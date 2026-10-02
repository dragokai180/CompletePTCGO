import asyncio
import unittest
from types import SimpleNamespace

from spirit.game.session.manager import GameSessionManager
from spirit.network.message_names import OutboundMsg


class _Client:
    def __init__(self, account_id):
        self.player = SimpleNamespace(account_id=account_id, username=account_id)
        self.addr = ("127.0.0.1", 1)
        self.packets = []

    async def send_packet(self, packet, request_id):
        self.packets.append((packet, request_id))


class VersusQueueWithoutBotTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.previous_instance = GameSessionManager._instance
        GameSessionManager._instance = None
        self.manager = GameSessionManager()

    async def asyncTearDown(self):
        for task in self.manager._background_tasks:
            task.cancel()
        GameSessionManager._instance = self.previous_instance

    async def test_waits_for_human_and_matches_second_player(self):
        first = _Client("first")
        second = _Client("second")
        self.manager._dispatch_ready_check = lambda *args: None

        await self.manager.add_to_queue(first, "Standard", {"deck": 1}, {}, 0)
        await asyncio.sleep(0)

        self.assertEqual(len(self.manager.queues["Standard"]), 1)
        self.assertFalse(self.manager._background_tasks)
        self.assertEqual(first.packets[0][0]["messageName"], OutboundMsg.MATCH_QUEUE_ENTERED.value)

        await self.manager.add_to_queue(second, "Standard", {"deck": 2}, {}, 0)
        self.assertFalse(self.manager.queues["Standard"])
        pairing = next(iter(self.manager.pending_pairings.values()))
        self.assertEqual(set(pairing["players"]), {"first", "second"})
        self.assertFalse(pairing["is_solo"])

    async def test_cancel_removes_waiting_player(self):
        client = _Client("first")
        await self.manager.add_to_queue(client, "Standard", {}, {}, 0)
        await self.manager.remove_from_queue(client)
        self.assertNotIn("Standard", self.manager.queues)
        self.assertEqual(client.packets[-1][0]["messageName"], OutboundMsg.MATCH_QUEUE_LEFT.value)


if __name__ == "__main__":
    unittest.main()
