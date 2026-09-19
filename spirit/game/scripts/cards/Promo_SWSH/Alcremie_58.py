from spirit.game.scripts.cards.SWSH2.Alcremie_87 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=58,
    rarity=Rarities.RarePromo,
    guid='e5ca76ae-d77f-5742-8a20-0fb04f38dd44',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH058'}
