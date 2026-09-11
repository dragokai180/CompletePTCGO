from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='bb354428-49ff-54d1-8b65-504d12c13bf0',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Blacksmith.Name',
    display_name='Blacksmith',
    searchable_by=['Blacksmith', 'Supporter', 'Blacksmith'],
    subtypes=['Supporter'],
    collector_number=88,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Attach 2 Fire Energy cards from your discard pile to 1 of your Fire Pokémon.'),
    condition=standard_trainer_condition('Attach 2 Fire Energy cards from your discard pile to 1 of your Fire Pokémon.'),
)
