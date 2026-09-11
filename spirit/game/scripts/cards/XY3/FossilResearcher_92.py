from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='2be42883-d054-599b-a803-32ff6d6faba9',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FossilResearcher.Name',
    display_name='Fossil Researcher',
    searchable_by=['Fossil Researcher', 'Supporter', 'FossilResearcher'],
    subtypes=['Supporter'],
    collector_number=92,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for up to 2 in any combination of Amaura or Tyrunt and put them onto your bench. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Search your deck for up to 2 in any combination of Amaura or Tyrunt and put them onto your bench. Shuffle your deck afterward.'),
)
