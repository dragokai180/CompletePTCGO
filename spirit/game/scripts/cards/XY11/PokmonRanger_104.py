from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='9f6fdde7-2978-541e-aa87-e53eb07019ce',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokmonRanger.Name',
    display_name='Pokémon Ranger',
    searchable_by=['Pokémon Ranger', 'Supporter', 'PokmonRanger'],
    subtypes=['Supporter'],
    collector_number=104,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Remove all effects of attacks on each player and his or her Pokémon.'),
    condition=standard_trainer_condition('Remove all effects of attacks on each player and his or her Pokémon.'),
)
