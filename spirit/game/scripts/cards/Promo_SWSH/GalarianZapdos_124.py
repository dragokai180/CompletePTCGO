from spirit.game.scripts.cards.SWSH7.GalarianZapdos_82 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=124,
    rarity=Rarities.RarePromo,
    guid='75bb502c-afce-5c27-9089-014ecaebee16',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH124'}
