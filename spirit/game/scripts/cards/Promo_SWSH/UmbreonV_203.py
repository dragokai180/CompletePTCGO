from spirit.game.scripts.cards.SWSH7.UmbreonV_94 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=203,
    rarity=Rarities.RarePromo,
    guid='17636335-8a18-5f2a-9c8f-5210fd517244',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH203'}
