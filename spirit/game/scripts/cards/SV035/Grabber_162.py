from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='73389d31-b4e7-588f-b546-34c0860bc136',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Grabber.Name',
    display_name='Grabber',
    searchable_by=['Grabber', 'Item', 'Grabber'],
    subtypes=['Item'],
    collector_number=162,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Your opponent reveals their hand, and you put a Pokémon you find there on the bottom of their deck.'),
    condition=standard_trainer_condition('Your opponent reveals their hand, and you put a Pokémon you find there on the bottom of their deck.'),
)
