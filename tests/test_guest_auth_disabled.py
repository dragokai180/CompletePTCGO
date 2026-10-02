import unittest
from unittest.mock import AsyncMock, patch

from spirit.network.message_names import OutboundMsg
from spirit.database.accounts import hash_password, is_legacy_guest_account
from spirit.packets.handlers.auth import AuthHandler


class _Client:
    def __init__(self):
        self.addr = ("127.0.0.1", 1234)
        self.packets = []

    async def send_packet(self, packet, request_id, **kwargs):
        self.packets.append((packet, request_id))


class GuestAuthDisabledTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.client = _Client()
        self.handler = AuthHandler(self.client)

    async def test_device_guest_and_mobile_routes_reject_without_database_access(self):
        with patch("spirit.packets.handlers.auth.run_db", new_callable=AsyncMock) as database:
            await self.handler.handle_start_authentication({"authType": "DeviceID"}, 1, 0)
            await self.handler.handle_gas_guest({"uniqueID": "device"}, 2, 0)
            await self.handler.handle_gas_mobile({"mobileID": "device"}, 3, 0)

        database.assert_not_awaited()
        self.assertEqual([request_id for _, request_id in self.client.packets], [1, 2, 3])
        self.assertTrue(all(packet["messageName"] == OutboundMsg.AUTH_FAILED.value
                            for packet, _ in self.client.packets))
        self.assertTrue(all("Guest access is disabled" in packet["reason"]["token"]
                            for packet, _ in self.client.packets))

    async def test_empty_credentials_cannot_create_an_account(self):
        with patch("spirit.packets.handlers.auth.run_db", new_callable=AsyncMock) as database:
            await self.handler.handle_gas_auth_token({"userID": "", "token": ""}, 4, 0)
        database.assert_not_awaited()
        self.assertEqual(self.client.packets[0][0]["messageName"], OutboundMsg.AUTH_FAILED.value)

    async def test_account_login_still_requests_token(self):
        await self.handler.handle_start_authentication({"authType": "GAS"}, 5, 0)
        self.assertEqual(self.client.packets[0][0]["messageName"], OutboundMsg.REQ_AUTH_TOKEN.value)

    async def test_legacy_guest_account_cannot_use_regular_login(self):
        account = {"password_hash": hash_password("guest_password")}
        self.assertTrue(is_legacy_guest_account(account))
        with patch("spirit.packets.handlers.auth.run_db", new_callable=AsyncMock, return_value=account) as database:
            await self.handler.handle_gas_auth_token({"userID": "old_guest", "token": "another_password"}, 6, 0)
        database.assert_awaited_once()
        self.assertEqual(self.client.packets[0][0]["messageName"], OutboundMsg.AUTH_FAILED.value)

    async def test_guest_default_password_cannot_create_regular_account(self):
        with patch("spirit.packets.handlers.auth.run_db", new_callable=AsyncMock) as database:
            await self.handler.handle_gas_auth_token({"userID": "new_user", "token": "guest_password"}, 7, 0)
        database.assert_not_awaited()
        self.assertEqual(self.client.packets[0][0]["messageName"], OutboundMsg.AUTH_FAILED.value)

    async def test_legacy_guest_account_cannot_use_cas_ticket(self):
        account = {"password_hash": hash_password("mobile_password")}
        with patch("spirit.packets.handlers.auth.consume_ticket", return_value=True), \
             patch("spirit.packets.handlers.auth.run_db", new_callable=AsyncMock, return_value=account):
            await self.handler.handle_authenticate_cas_ticket(
                {"accountName": "old_mobile", "serviceTicket": "ST-test", "serviceName": "game"}, 8, 0)
        self.assertEqual(self.client.packets[0][0]["messageName"], OutboundMsg.AUTH_FAILED.value)


if __name__ == "__main__":
    unittest.main()
