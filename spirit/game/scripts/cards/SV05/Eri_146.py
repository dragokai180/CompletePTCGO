from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="ab0f7bac-ab92-5297-83e3-06e13189ae8e",
    key="SV05",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Eri.Name",
    display_name="Eri",
    searchable_by=["Eri", "Supporter", "Eri"],
    subtypes=["Supporter"],
    collector_number=146,
    set_code="SV05",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Your opponent reveals their hand, and you discard up to 2 Item cards you find there."),
)
