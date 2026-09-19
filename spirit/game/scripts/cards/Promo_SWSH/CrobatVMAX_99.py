from spirit.game.scripts.cards.SWSH45.CrobatVMAX_45 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=99,
    rarity=Rarities.RarePromo,
    guid='ec23e316-2c7f-5473-88bc-2b25885b04da',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH099'}
