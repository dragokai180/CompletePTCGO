from spirit.game.scripts.cards.SWSH7.FlareonVMAX_18 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=180,
    rarity=Rarities.RarePromo,
    guid='b1b966c6-d607-599a-8d4b-0d9d493dbbd7',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH180'}
