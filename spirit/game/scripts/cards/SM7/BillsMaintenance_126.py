from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import PokemonTypes, Rarities
from spirit.game.card_effects.standard_era import (
    standard_attack, standard_passive, standard_stadium_ability,
    standard_trainer_condition, standard_trainer_effect,
)


card = SupporterCardDef(
    guid='e00628fa-11fb-58c3-9b08-38955c6747ab',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.trainer.BillsMaintenance.Name',
    display_name="Bill's Maintenance",
    searchable_by=["Bill's Maintenance", 'Supporter', 'BillsMaintenance'],
    subtypes=['Supporter'],
    collector_number=126,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=standard_trainer_effect('Shuffle a card from your hand into your deck. If you do, draw 3 cards.'),
    condition=standard_trainer_condition('Shuffle a card from your hand into your deck. If you do, draw 3 cards.'),
)
