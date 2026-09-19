from spirit.game.scripts.cards.SWSH3.EternatusVMAX_117 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=45,
    rarity=Rarities.RarePromo,
    guid='dc49061b-83f8-5ded-b2fa-b3ab756f9c62',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH045'}
