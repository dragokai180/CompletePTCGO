from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='6b7d0bfc-a78a-5fd6-9d2d-bf502534705e',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.trainer.FossilExcavationMap.Name',
    display_name='Fossil Excavation Map',
    searchable_by=['Fossil Excavation Map', 'Item', 'FossilExcavationMap'],
    subtypes=['Item'],
    collector_number=107,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Choose 1:\n• Search your deck for an Unidentified Fossil card, reveal it, and put it into your hand. Then, shuffle your deck.\n• Put an Unidentified Fossil card from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Choose 1:\n• Search your deck for an Unidentified Fossil card, reveal it, and put it into your hand. Then, shuffle your deck.\n• Put an Unidentified Fossil card from your discard pile into your hand. You may play as many Item cards as you like during your turn (before your attack).'),
)
