from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='8a3e2994-58bf-59b4-919b-4f47f20aeccf',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Channeler.Name',
    display_name='Channeler',
    searchable_by=['Channeler', 'Supporter', 'Channeler'],
    subtypes=['Supporter'],
    collector_number=190,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Remove all effects of attacks on you and each of your Pokémon.'),
    condition=standard_trainer_condition('Remove all effects of attacks on you and each of your Pokémon.'),
)
