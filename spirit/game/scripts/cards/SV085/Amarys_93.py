from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="fdfb7912-e175-5a6b-9168-99ad4b4c0b8e",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Amarys.Name",
    display_name="Amarys",
    searchable_by=["Amarys", "Supporter", "Amarys"],
    subtypes=["Supporter"],
    collector_number=93,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.Common,
    effect=standard_trainer_effect("Draw 4 cards. At the end of this turn, if you have 5 or more cards in your hand, discard your hand."),
)
