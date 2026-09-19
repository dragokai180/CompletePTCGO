from spirit.game.scripts.cards.SWSH5.Octillery_37 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=89,
    rarity=Rarities.RarePromo,
    guid='5e8a6528-bad1-5e32-9dc7-dc33d3abe052',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH089'}
