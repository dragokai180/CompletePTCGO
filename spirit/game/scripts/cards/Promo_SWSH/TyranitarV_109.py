from spirit.game.scripts.cards.SWSH5.TyranitarV_97 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=109,
    rarity=Rarities.RarePromo,
    guid='2f86bc5e-1f71-5cc6-a38f-50597452c7b1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH109'}
