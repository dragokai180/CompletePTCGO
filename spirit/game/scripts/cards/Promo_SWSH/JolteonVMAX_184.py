from spirit.game.scripts.cards.SWSH7.JolteonVMAX_51 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=184,
    rarity=Rarities.RarePromo,
    guid='de20d58b-4569-54b7-923f-26919e2fc678',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH184'}
