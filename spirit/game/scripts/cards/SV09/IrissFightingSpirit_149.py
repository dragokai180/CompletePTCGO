from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="ccc7d3fe-cb27-5236-a495-8dc671e16bc4",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IrissFightingSpirit.Name",
    display_name="Iris's Fighting Spirit",
    searchable_by=["Iris's Fighting Spirit", "Supporter", "IrissFightingSpirit"],
    subtypes=["Supporter"],
    collector_number=149,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("You can use this card only if you discard another card from your hand.  Draw cards until you have 6 cards in your hand."),
)
