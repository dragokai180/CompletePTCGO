from spirit.game.scripts.cards.SWSH1.Marnie_169 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=120,
    rarity=Rarities.RarePromo,
    guid='d4afe501-a630-5eea-bdcb-d0cda3d74e47',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH120'}
