from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='ae5aff8d-6e25-5337-be44-b61d399090c0',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.LureBall.Name',
    display_name='Lure Ball',
    searchable_by=['Lure Ball', 'Item', 'LureBall'],
    subtypes=['Item'],
    collector_number=138,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip 3 coins. For each heads, put an Evolution Pokémon from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Flip 3 coins. For each heads, put an Evolution Pokémon from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)
