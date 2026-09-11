import unittest

from spirit.game.session.game_session import _should_auto_take_all_prizes


class AutomaticPrizeAwardTests(unittest.TestCase):
    def test_last_prize_is_automatic(self):
        self.assertTrue(_should_auto_take_all_prizes(1, 1, None, True))

    def test_multi_prize_knockout_that_wins_is_automatic(self):
        self.assertTrue(_should_auto_take_all_prizes(2, 3, None, True))

    def test_non_winning_award_still_allows_the_player_to_choose(self):
        self.assertFalse(_should_auto_take_all_prizes(3, 2, None, True))

    def test_optional_up_to_effect_keeps_its_choice(self):
        self.assertFalse(_should_auto_take_all_prizes(2, 2, 0, True))

    def test_undealt_test_pile_is_not_treated_as_a_win(self):
        self.assertFalse(_should_auto_take_all_prizes(1, 1, None, False))


if __name__ == "__main__":
    unittest.main()
