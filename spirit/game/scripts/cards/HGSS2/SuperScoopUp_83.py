from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='acf0b955-5332-5671-9dc3-7dbe78e81a98',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.trainer.SuperScoopUp.Name',
    display_name='Super Scoop Up',
    searchable_by=['Super Scoop Up', 'Item', 'SuperScoopUp'],
    subtypes=['Item'],
    collector_number=83,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip a coin. If heads, return 1 of your Pokémon and all cards attached to it to your hand.'),
    condition=standard_trainer_condition('Flip a coin. If heads, return 1 of your Pokémon and all cards attached to it to your hand.'),
)
