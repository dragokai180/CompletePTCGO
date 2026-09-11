from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='5e94fa4a-54ad-5206-864e-f34de06f53a2',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RotomDex.Name',
    display_name='Rotom Dex',
    searchable_by=['Rotom Dex', 'Item', 'RotomDex'],
    subtypes=['Item'],
    collector_number=131,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('After counting your Prize cards, shuffle them into your deck. Then, take that many cards from the top of your deck and put them face down as your Prize cards. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('After counting your Prize cards, shuffle them into your deck. Then, take that many cards from the top of your deck and put them face down as your Prize cards. You may play as many Item cards as you like during your turn (before your attack).'),
)
