from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='21dff0ef-6275-5b93-b3eb-171cd14943b8',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RotomDexPokFinderMode.Name',
    display_name='Rotom Dex Poké Finder Mode',
    searchable_by=['Rotom Dex Poké Finder Mode', 'Item', 'RotomDexPokFinderMode'],
    subtypes=['Item'],
    collector_number=122,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Look at the top 4 cards of your deck and put them back in any order or shuffle them into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Look at the top 4 cards of your deck and put them back in any order or shuffle them into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
