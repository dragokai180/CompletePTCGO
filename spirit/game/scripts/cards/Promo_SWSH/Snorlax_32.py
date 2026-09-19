from spirit.game.scripts.cards.SWSH1.Snorlax_140 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=32,
    rarity=Rarities.RarePromo,
    guid='34638183-1e71-58f1-8ff7-48505b8d680a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH032'}
