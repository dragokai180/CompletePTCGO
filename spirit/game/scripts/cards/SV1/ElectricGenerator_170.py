from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='cdf66ab1-eee4-508e-b3b0-5c09c6455f21',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ElectricGenerator.Name',
    display_name='Electric Generator',
    searchable_by=['Electric Generator', 'Item', 'ElectricGenerator'],
    subtypes=['Item'],
    collector_number=170,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 5 cards of your deck and attach up to 2 Basic Lightning Energy cards you find there to your Benched Lightning Pokémon in any way you like. Shuffle the other cards back into your deck.'),
    condition=standard_trainer_condition('Look at the top 5 cards of your deck and attach up to 2 Basic Lightning Energy cards you find there to your Benched Lightning Pokémon in any way you like. Shuffle the other cards back into your deck.'),
)
