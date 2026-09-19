from spirit.game.scripts.cards.SWSH6.Klara_145 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=302,
    rarity=Rarities.RarePromo,
    guid='72893bca-b7eb-52be-b268-382841a060d2',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH302'}
