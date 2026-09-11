from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='5d36af85-9b3d-50d4-9078-07db64b03353',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.EnergyRecycleSystem.Name',
    display_name='Energy Recycle System',
    searchable_by=['Energy Recycle System', 'Item', 'EnergyRecycleSystem'],
    subtypes=['Item'],
    collector_number=128,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose 1:\n• Put a basic Energy card from your discard pile into your hand.\n• Shuffle 3 basic Energy cards from your discard pile into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Choose 1:\n• Put a basic Energy card from your discard pile into your hand.\n• Shuffle 3 basic Energy cards from your discard pile into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
