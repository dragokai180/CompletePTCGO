from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='e4c3219c-86a4-5916-b99c-b1f96a23f8a8',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.trainer.CherishBall.Name',
    display_name='Cherish Ball',
    searchable_by=['Cherish Ball', 'Item', 'CherishBall'],
    subtypes=['Item'],
    collector_number=191,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Search your deck for a Pokémon-GX, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Search your deck for a Pokémon-GX, reveal it, and put it into your hand. Then, shuffle your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
