from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='c102cb21-1255-5094-95c7-7525ec80e694',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.MegaCatcher.Name',
    display_name='Mega Catcher',
    searchable_by=['Mega Catcher', 'Item', 'MegaCatcher'],
    subtypes=['Item'],
    collector_number=104,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Switch 1 of your opponent's Benched Mega Evolution Pokémon with his or her Active Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Switch 1 of your opponent's Benched Mega Evolution Pokémon with his or her Active Pokémon. You may play as many Item cards as you like during your turn (before your attack)."),
)
