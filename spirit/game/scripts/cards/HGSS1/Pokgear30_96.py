from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='176e5110-fd93-5c42-ac41-09ef81ec482c',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Pokgear30.Name',
    display_name='Pokégear 3.0',
    searchable_by=['Pokégear 3.0', 'Item', 'Pokgear30'],
    subtypes=['Item'],
    collector_number=96,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 7 cards of your deck. Choose a Supporter card you find there, show it to your opponent, and put it into your hand. Shuffle the other cards back into your deck.'),
    condition=standard_trainer_condition('Look at the top 7 cards of your deck. Choose a Supporter card you find there, show it to your opponent, and put it into your hand. Shuffle the other cards back into your deck.'),
)
