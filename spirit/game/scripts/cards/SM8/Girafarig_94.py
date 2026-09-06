"""Girafarig (SM - Lost Thunder 94/214).

Basic Psychic Pokemon. HP 90, weakness Psychic x2, no resistance, retreat 1.

  Get Lost   [C]      Put 2 cards from your opponent's discard pile in the
                      Lost Zone.
  Mind Shock [CCC] 70 This attack's damage isn't affected by Weakness or
                      Resistance.

Get Lost is Lysandre {*} with a flat count instead of one read off the
board, so both go through lost_zone_from_opponent_discard.

Mind Shock waives Weakness and Resistance and nothing else, so it is a
plain deal_damage with both flags rather than ignore_effects_attack, which
would also strip the defender's damage-reduction effects. Note the waiver
cuts both ways here: Girafarig is Psychic and weak to Psychic, so a
Psychic mirror gives up its own x2 by attacking with this.
"""

from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import lost_zone_from_opponent_discard


async def mind_shock(ctx):
    """70, unaffected by Weakness or Resistance."""
    await ctx.deal_damage(ignore_weakness=True, ignore_resistance=True)


card = PokemonCardDef(
    guid="1af1547f-bcba-5dee-98e6-ddcf73045284",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Girafarig.Name",
    display_name="Girafarig",
    searchable_by=["Girafarig", "Basic", "Girafarig"],
    subtypes=["Basic"],
    collector_number=94,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=203,
    abilities=[
        Attack(
            title="Get Lost",
            game_text="Put 2 cards from your opponent's discard pile in the Lost Zone.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=lost_zone_from_opponent_discard(2),
        ),
        Attack(
            title="Mind Shock",
            game_text="This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=mind_shock,
        ),
    ],
)
