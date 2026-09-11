from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="147df5d2-cde1-5924-9a09-e2bf34834437",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Ortega.Name",
    display_name="Ortega",
    searchable_by=["Ortega", "Supporter", "Ortega"],
    subtypes=["Supporter"],
    collector_number=141,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.RareUltra,
    effect=standard_trainer_effect("Your opponent reveals their hand, and you choose a card you find there and put it on the bottom of their deck. If you put a card on the bottom of your opponent's deck in this way, your opponent may draw a card."),
)
