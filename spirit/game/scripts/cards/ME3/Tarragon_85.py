from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="84621173-4cda-5ccb-ba88-9199aa37e3dd",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Tarragon.Name",
    display_name="Tarragon",
    searchable_by=["Tarragon", "Supporter", "Tarragon"],
    subtypes=["Supporter"],
    collector_number=85,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put up to 4 in any combination of Fighting Pokémon and Basic Fighting Energy cards from your discard pile into your hand."),
)
