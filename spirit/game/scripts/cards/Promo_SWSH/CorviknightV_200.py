from spirit.game.scripts.cards.SWSH5.CorviknightV_109 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=200,
    rarity=Rarities.RarePromo,
    guid='b0c9b7a5-2e6b-5777-b68e-73c469393609',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH200'}
