from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = ItemCardDef(
    guid='6957d25d-fda7-5fb4-8096-e34502d64d7d',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.trainer.TormentingSpray.Name',
    display_name='Tormenting Spray',
    searchable_by=['Tormenting Spray', 'Item', 'TormentingSpray'],
    subtypes=['Item'],
    collector_number=125,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect("Choose a random card from your opponent's hand. Your opponent reveals that card. If it's a Supporter card, discard it. You may play as many Item cards as you like during your turn (before your attack)."),
    condition=standard_trainer_condition("Choose a random card from your opponent's hand. Your opponent reveals that card. If it's a Supporter card, discard it. You may play as many Item cards as you like during your turn (before your attack)."),
)
