from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='a21675b6-9b09-5d9d-b191-183260ce7063',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.RollerSkater.Name',
    display_name='Roller Skater',
    searchable_by=['Roller Skater', 'Supporter', 'RollerSkater'],
    subtypes=['Supporter'],
    collector_number=203,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Discard a card from your hand. If you do, draw 2 cards. If you discarded an Energy card in this way, draw 2 more cards.'),
    condition=standard_trainer_condition('Discard a card from your hand. If you do, draw 2 cards. If you discarded an Energy card in this way, draw 2 more cards.'),
)
