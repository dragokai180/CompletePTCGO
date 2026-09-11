from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='39e9f59b-c13e-5f3c-ae47-dc6d8d834dd3',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.trainer.Electrocharger.Name',
    display_name='Electrocharger',
    searchable_by=['Electrocharger', 'Item', 'Electrocharger'],
    subtypes=['Item'],
    collector_number=139,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Flip 2 coins. For each heads, shuffle an Electropower card from your discard pile into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
    condition=standard_trainer_condition('Flip 2 coins. For each heads, shuffle an Electropower card from your discard pile into your deck. You may play as many Item cards as you like during your turn (before your attack).'),
)
