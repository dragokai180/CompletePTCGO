from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='0348e1db-4ecb-513f-a4a5-d205e26ab877',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavationKit.Name',
    display_name='Fossil Excavation Kit',
    searchable_by=['Fossil Excavation Kit', 'Item', 'FossilExcavationKit'],
    subtypes=['Item'],
    collector_number=101,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put 2 in any combination of Helix Fossil Omanyte, Dome Fossil Kabuto, or Old Amber Aerodactyl cards from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Put 2 in any combination of Helix Fossil Omanyte, Dome Fossil Kabuto, or Old Amber Aerodactyl cards from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)
