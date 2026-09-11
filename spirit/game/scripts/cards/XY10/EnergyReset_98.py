from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='5519f2fa-f23f-5eb2-93b0-9d5d836802de',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EnergyReset.Name',
    display_name='Energy Reset',
    searchable_by=['Energy Reset', 'Item', 'EnergyReset'],
    subtypes=['Item'],
    collector_number=98,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Put as many Energy attached to your Pokémon as you like into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Put as many Energy attached to your Pokémon as you like into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)
