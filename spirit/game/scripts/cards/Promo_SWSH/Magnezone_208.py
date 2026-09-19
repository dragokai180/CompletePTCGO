from spirit.game.scripts.cards.SWSH10.Magnezone_107 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=208,
    rarity=Rarities.RarePromo,
    guid='e5b89136-2695-5538-a312-5ea247873f7c',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH208'}
