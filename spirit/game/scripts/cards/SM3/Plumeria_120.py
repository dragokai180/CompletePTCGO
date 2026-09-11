from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='081907e9-09b4-59a9-be15-a5d82e91d927',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Plumeria.Name',
    display_name='Plumeria',
    searchable_by=['Plumeria', 'Supporter', 'Plumeria'],
    subtypes=['Supporter'],
    collector_number=120,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Discard 2 cards from your hand. If you do, discard an Energy from 1 of your opponent's Pokémon."),
    condition=standard_trainer_condition("Discard 2 cards from your hand. If you do, discard an Energy from 1 of your opponent's Pokémon."),
)
