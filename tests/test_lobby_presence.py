"""Chat membership survives repeated requests without leaving ghost users."""
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, Mock, patch

from spirit.network.message_names import OutboundMsg
from spirit.packets.handlers.social import SocialHandler, LOBBY_ROOMS


ROOM = LOBBY_ROOMS[0]["roomID"]


class LobbyPresenceTests(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.server = SimpleNamespace(clients=[])
        self.observer = self.client("observer", {ROOM})
        self.user = self.client("sunandmoon")
        self.handler = SocialHandler(self.user)

    def client(self, account, rooms=()):
        client = SimpleNamespace(
            server=self.server, running=True, addr=("localhost", 1),
            player=SimpleNamespace(account_id=account, screen_name=account),
            chat_rooms=set(rooms), send_packet=AsyncMock(),
        )
        self.server.clients.append(client)
        return client

    async def test_repeated_join_notifies_peers_only_once(self):
        for rid in (1, 2):
            await self.handler.handle_join_room({"roomID": ROOM}, rid, 0)
        self.observer.send_packet.assert_awaited_once()
        self.assertEqual(self.observer.send_packet.call_args.args[0]["messageName"],
                         OutboundMsg.NOTIFY_JOIN.value)
        self.assertEqual(self.user.send_packet.await_count, 2)
        members = self.user.send_packet.call_args.args[0]["members"]
        self.assertEqual(len(members), 2)

    async def test_disconnect_notifies_each_room_once(self):
        self.user.chat_rooms.update((ROOM, "second"))
        self.observer.chat_rooms.add("second")
        self.user.running = False
        await self.handler.leave_all_rooms()
        await self.handler.leave_all_rooms()
        self.assertEqual(self.user.chat_rooms, set())
        packets = [call.args[0] for call in self.observer.send_packet.call_args_list]
        self.assertEqual({p["roomID"] for p in packets}, {ROOM, "second"})
        self.assertEqual(len(packets), 2)
        self.assertTrue(all(p["messageName"] == OutboundMsg.NOTIFY_LEAVE.value
                            and p["accountID"] == "sunandmoon" for p in packets))

    async def test_old_disconnect_does_not_remove_replacement(self):
        self.user.chat_rooms.add(ROOM)
        self.user.running = False
        self.client("sunandmoon", {ROOM})
        await self.handler.leave_all_rooms()
        self.observer.send_packet.assert_not_awaited()
        self.assertFalse(self.user.chat_rooms)

    async def test_shutdown_clears_without_notifications(self):
        self.user.chat_rooms.add(ROOM)
        await self.handler.leave_all_rooms(notify=False)
        self.assertFalse(self.user.chat_rooms)
        self.observer.send_packet.assert_not_awaited()

    async def test_roster_excludes_dead_clients_and_duplicate_accounts(self):
        dead = self.client("dead", {ROOM})
        dead.running = False
        self.client("observer", {ROOM})
        await self.handler.handle_join_room({"roomID": ROOM}, 1, 0)
        members = self.user.send_packet.call_args.args[0]["members"]
        self.assertEqual([p["accountID"] for p in members], ["observer", "sunandmoon"])
        dead.send_packet.assert_not_awaited()

    async def test_disconnect_calls_room_cleanup(self):
        from spirit.server.client_handler import ClientHandler
        self.user.chat_rooms.add(ROOM)
        self.user.writer = SimpleNamespace(close=Mock(), wait_closed=AsyncMock())
        self.server.remove_client = Mock()
        manager = Mock()
        manager.remove_from_queue = AsyncMock()
        manager.remove_challenges_for_client = AsyncMock()
        manager.get_session_by_player_id.return_value = None
        tournament = SimpleNamespace(handle_disconnect=AsyncMock())
        with patch("spirit.server.client_handler.GameSessionManager", return_value=manager), \
             patch("spirit.game.live_tournament.LiveTournamentManager", return_value=tournament), \
             patch.object(SocialHandler, "broadcast_presence", new_callable=AsyncMock):
            await ClientHandler.disconnect(self.user)
        self.observer.send_packet.assert_awaited_once()
        self.assertEqual(self.observer.send_packet.call_args.args[0]["messageName"],
                         OutboundMsg.NOTIFY_LEAVE.value)
        self.server.remove_client.assert_called_once_with(self.user)


if __name__ == "__main__":
    unittest.main()
