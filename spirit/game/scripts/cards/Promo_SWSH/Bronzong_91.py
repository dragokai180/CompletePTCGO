from spirit.game.scripts.cards.SWSH5.Bronzong_102 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=91,
    rarity=Rarities.RarePromo,
    guid='97b0bf9b-4bee-5d10-9fce-054a181a23be',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH091'}
