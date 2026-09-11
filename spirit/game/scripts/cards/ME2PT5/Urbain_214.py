from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="7fd00d63-eee8-5c38-9c28-8f75ad044e1b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Urbain.Name",
    display_name="Urbain",
    searchable_by=["Urbain", "Supporter", "Urbain"],
    subtypes=["Supporter"],
    collector_number=214,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Draw 3 cards."),
)
