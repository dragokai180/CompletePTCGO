from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_effect,
)


card = SupporterCardDef(
    guid="8b15d6e8-d77a-5428-b6db-ef0fe48c8bcd",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.trainer.ProfessorTurosScenario.Name",
    display_name="Professor Turo's Scenario",
    searchable_by=["Professor Turo's Scenario", "Supporter", "Future", "ProfessorTurosScenario"],
    subtypes=["Supporter", "Future"],
    collector_number=121,
    set_code="SV085",
    regulation_mark="G",
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Put 1 of your Pokémon in play into your hand. (Discard all cards attached to that Pokémon.)"),
)
