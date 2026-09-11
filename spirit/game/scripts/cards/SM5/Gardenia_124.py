from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='54942e2f-c703-50ee-b634-7b23d5a46a45',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Gardenia.Name',
    display_name='Gardenia',
    searchable_by=['Gardenia', 'Supporter', 'Gardenia'],
    subtypes=['Supporter'],
    collector_number=124,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Heal 80 damage from 1 of your Pokémon that has any Grass Energy attached to it.'),
    condition=standard_trainer_condition('Heal 80 damage from 1 of your Pokémon that has any Grass Energy attached to it.'),
)
