"""Stealthy Hood (SM - Unbroken Bonds 186/214).

Pokemon Tool.

  "Prevent all effects of your opponent's Abilities done to the Pokemon this
   card is attached to. Remove any such existing effects."

Hide 'n' Sneak's shield with the attack half removed: FullEffectShieldPassive
answers both blocks_attack_effects and blocks_ability_effects, this one only
the second, so it sits beside it in passives_common as
AbilityEffectShieldPassive.

The point of the card is Garbotoxin, and that needed wiring. Turning an
Ability off is an effect of an Ability, but the engine asks about it through
blocks_abilities rather than through the effect shield, so ability_locked
and active_passives now skip an opposing Pokemon's lock when the target is
hooded. A Stadium lock is not an Ability, so Silent Lab still silences the
holder; nor is your own Garbodor an opponent's Ability, so it still silences
your own hooded Pokemon. Wobbuffet's Bide Barricade, being an opposing
Pokemon's Ability, is stopped.

NOT modelled: "Remove any such existing effects." A lock lifts by itself the
moment the Hood goes on, because it is re-read on every query, but an effect
already spent -- damage counters an Ability placed, a card it already
discarded -- cannot be taken back.
"""

from spirit.game.data_utils import PokemonToolCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.passives_common import ability_effect_shield_passive

card = PokemonToolCardDef(
    guid="54bb7825-24ff-5e2d-bc5f-48985460adc4",
    key="SM10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.StealthyHood.Name",
    display_name="Stealthy Hood",
    searchable_by=["Stealthy Hood", "Pokémon Tool", "StealthyHood"],
    subtypes=["Pokémon Tool"],
    collector_number=186,
    set_code="SM10",
    rarity=Rarities.Uncommon,
    passive=ability_effect_shield_passive(),
)
