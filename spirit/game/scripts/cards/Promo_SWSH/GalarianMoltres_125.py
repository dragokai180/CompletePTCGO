from spirit.game.scripts.cards.SWSH7.GalarianMoltres_93 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=125,
    rarity=Rarities.RarePromo,
    guid='d68f0d9e-6293-5db8-ab07-d581753bf992',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH125'}
