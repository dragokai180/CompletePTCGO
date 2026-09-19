from spirit.game.scripts.cards.SWSH1.Noctowl_144 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=27,
    rarity=Rarities.RarePromo,
    guid='0eb1c183-a253-57d7-9a9a-a300d22b403f',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH027'}
