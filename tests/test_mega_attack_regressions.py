import unittest

from spirit.game.scripts.cards.ME4.Metagross_61 import metallic_hammer


class _CopiedMetallicHammerContext:
    def __init__(self):
        self.attacker = object()
        self.prompted = False
        self.discard_requested = False
        self.damage = None

    async def ask_yes_no(self, prompt):
        self.prompted = True
        return True

    async def discard_energy_from(self, pokemon, count, predicate=None, prompt=""):
        self.discard_requested = True
        return []

    async def deal_damage(self, amount):
        self.damage = amount


class MegaAttackRegressionTests(unittest.IsolatedAsyncioTestCase):
    async def test_copied_metallic_hammer_can_choose_rider_without_metal_energy(self):
        ctx = _CopiedMetallicHammerContext()

        await metallic_hammer(ctx)

        self.assertTrue(ctx.prompted)
        self.assertTrue(ctx.discard_requested)
        self.assertEqual(ctx.damage, 300)


if __name__ == "__main__":
    unittest.main()
