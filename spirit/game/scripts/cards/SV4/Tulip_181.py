from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='aeb561b6-8d1f-5d13-b887-ae0ee4c0bccc',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Tulip.Name',
    display_name='Tulip',
    searchable_by=['Tulip', 'Supporter', 'Tulip'],
    subtypes=['Supporter'],
    collector_number=181,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put up to 4 in any combination of Psychic Pokémon and Basic Psychic Energy cards from your discard pile into your hand.'),
    condition=standard_trainer_condition('Put up to 4 in any combination of Psychic Pokémon and Basic Psychic Energy cards from your discard pile into your hand.'),
)
