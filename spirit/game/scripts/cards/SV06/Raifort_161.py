from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="6e417334-b803-5531-b7d6-ad13fd298712",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Raifort.Name",
    display_name="Raifort",
    searchable_by=["Raifort", "Supporter", "Raifort"],
    subtypes=["Supporter"],
    collector_number=161,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Look at the top 5 cards of your deck and discard any number of them. Put the other cards back in any order."),
)
