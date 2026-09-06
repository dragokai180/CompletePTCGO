"""Muscle Band (XY 121/146).

  "The attacks of the Pokemon this card is attached to do 20 more damage
   to your opponent's Active Pokemon (before applying Weakness and
   Resistance)."

Vitality Band with 20 instead of 10 -- same helper, same predicate
(lambda t: True, i.e. every target type, unlike the type-gated Gloves the
helper is named for). TypedDamageBoostPassive already matches the printed
wording: it only fires for the holder's own attacks (calc.is_attack,
carrier_pokemon is calc.attacker), only against the opponent (is_opposing),
only on the Active (to_active_only, the helper's default), and it adds to
calc.amount before weakness/resistance are applied.
"""

from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import typed_damage_boost_tool

card = PokemonToolCardDef(
    guid="80e07131-c5de-5aa2-9077-42d702d02f56",
    key="XY1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MuscleBand.Name",
    display_name="Muscle Band",
    searchable_by=["Muscle Band", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=121,
    set_code="XY1",
    rarity=Rarities.Uncommon,
    passive=typed_damage_boost_tool(lambda t: True, 20),
)
