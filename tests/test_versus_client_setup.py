import unittest
from types import SimpleNamespace
from unittest.mock import patch

from spirit.game.account_attributes import VISITED_SCENES_ATTRIBUTE, build_account_attributes
from spirit.game.attributes import AttrID
from spirit.network.message_names import OutboundMsg
from spirit.packets.handlers.data_sync import DataSyncHandler


class VersusClientSetupTests(unittest.TestCase):
    def test_constructed_deck_tutorial_is_marked_visited(self):
        with patch("spirit.game.account_attributes.VersusSeasonManager") as seasons, \
             patch("spirit.game.account_attributes.versus_data.get_progress", return_value=(0, 0)), \
             patch("spirit.game.account_attributes.get_account_settings", return_value={}), \
             patch("spirit.game.account_attributes.get_screen_name", return_value="Player"):
            seasons.return_value.get_active_season.return_value = None
            attributes = build_account_attributes("account")

        by_name = {attribute["name"]: attribute["value"] for attribute in attributes}
        self.assertIn("VersusUpdate", by_name[VISITED_SCENES_ATTRIBUTE])
        self.assertEqual(by_name[AttrID.ACCOUNT_SETTINGS.value], {})


class WalletCapTests(unittest.IsolatedAsyncioTestCase):
    async def test_wallet_request_sends_token_cap_before_balance(self):
        class Client:
            def __init__(self):
                self.packets = []
                self.player = SimpleNamespace(
                    wallet=True,
                    get_wallet_data=lambda: {"currencies": [
                        {"name": AttrID.TRAINER_TOKENS.value, "value": 1000}
                    ]},
                )

            async def send_packet(self, packet, request_id, **kwargs):
                self.packets.append(packet)

        client = Client()
        await DataSyncHandler(client).handle_get_wallet({}, 5, 0)
        self.assertEqual([p["messageName"] for p in client.packets],
                         [OutboundMsg.CURRENCY_CAPS.value, OutboundMsg.CURRENT_WALLET.value])
        cap = client.packets[0]["currencies"][0]
        self.assertEqual(cap["name"], AttrID.TRAINER_TOKENS.value)
        self.assertGreater(cap["value"], client.packets[1]["currencies"][0]["value"])


if __name__ == "__main__":
    unittest.main()
