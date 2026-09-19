from spirit.game.scripts.cards.SWSH10.HisuianTyphlosionV_53 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=237,
    rarity=Rarities.RarePromo,
    guid='b94e11eb-01e5-5f56-b213-1b880170ebc0',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH237'}
