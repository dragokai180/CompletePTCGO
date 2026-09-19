from spirit.game.scripts.cards.SWSH10.OriginFormeDialgaVSTAR_114 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=256,
    rarity=Rarities.RarePromo,
    guid='7b00d8af-9229-5f5a-bcb5-603fc4c8a421',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH256'}
