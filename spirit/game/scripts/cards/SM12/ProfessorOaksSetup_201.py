from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='4d13404d-e3ba-599c-9796-9bd2c3ac4808',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorOaksSetup.Name',
    display_name="Professor Oak's Setup",
    searchable_by=["Professor Oak's Setup", 'Supporter', 'ProfessorOaksSetup'],
    subtypes=['Supporter'],
    collector_number=201,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 3 Basic Pokémon of different types and put them onto your Bench. Then, shuffle your deck.'),
    condition=standard_trainer_condition('Search your deck for up to 3 Basic Pokémon of different types and put them onto your Bench. Then, shuffle your deck.'),
)
