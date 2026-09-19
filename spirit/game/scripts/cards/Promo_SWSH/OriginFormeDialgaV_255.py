from spirit.game.scripts.cards.SWSH10.OriginFormeDialgaV_113 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=255,
    rarity=Rarities.RarePromo,
    guid='bf3329d0-26b5-5af8-9159-bac29078a8ab',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH255'}
