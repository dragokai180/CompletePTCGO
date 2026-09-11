from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='80f9f7ad-fa3f-5a91-be6f-13dd5601d449',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.trainer.PokBall.Name',
    display_name='Poké Ball',
    searchable_by=['Poké Ball', 'Item', 'PokBall'],
    subtypes=['Item'],
    collector_number=95,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.'),
    condition=standard_trainer_condition('Flip a coin. If heads, search your deck for a Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.'),
)
