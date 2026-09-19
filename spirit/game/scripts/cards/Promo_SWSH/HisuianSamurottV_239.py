from spirit.game.scripts.cards.SWSH10.HisuianSamurottV_101 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=239,
    rarity=Rarities.RarePromo,
    guid='6157b117-5b45-5805-b845-92c23633156a',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH239'}
