from spirit.game.scripts.cards.SWSH4.PikachuV_43 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=61,
    rarity=Rarities.RarePromo,
    guid='bc84d6b5-9526-544e-94fb-700c70c8d030',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH061'}
