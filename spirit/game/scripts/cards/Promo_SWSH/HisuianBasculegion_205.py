from spirit.game.scripts.cards.SWSH10.HisuianBasculegion_44 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=205,
    rarity=Rarities.RarePromo,
    guid='374a7c83-5f0b-533b-b336-4db7c1a84a74',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH205'}
