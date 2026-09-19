from spirit.game.scripts.cards.SWSH10.Wyrdeer_69 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=206,
    rarity=Rarities.RarePromo,
    guid='4c870cfc-6d59-5e1c-9eeb-ab7ac248d9de',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH206'}
