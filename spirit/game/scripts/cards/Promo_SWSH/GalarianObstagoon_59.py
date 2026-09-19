from spirit.game.scripts.cards.SWSH1.GalarianObstagoon_119 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=59,
    rarity=Rarities.RarePromo,
    guid='c323843e-4f66-539e-bde6-eef500d620ec',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH059'}
