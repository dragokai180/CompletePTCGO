from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='a4ae3295-5f22-5d38-b7ed-7319d47bb764',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.DualBall.Name',
    display_name='Dual Ball',
    searchable_by=['Dual Ball', 'Item', 'DualBall'],
    subtypes=['Item'],
    collector_number=72,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip 2 coins. For each heads, search your deck for a Basic Pokémon, show it to your opponent, and put it into your hand. If you do, shuffle your deck afterward.'),
    condition=standard_trainer_condition('Flip 2 coins. For each heads, search your deck for a Basic Pokémon, show it to your opponent, and put it into your hand. If you do, shuffle your deck afterward.'),
)
