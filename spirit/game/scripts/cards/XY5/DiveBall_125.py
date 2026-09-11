from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ff945cff-af8d-5a5a-af6e-ba30662bf1fe',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DiveBall.Name',
    display_name='Dive Ball',
    searchable_by=['Dive Ball', 'Item', 'DiveBall'],
    subtypes=['Item'],
    collector_number=125,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Water Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for a Water Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward. You may play as many Item cards as you like during your turn (before your attack).'),
)
