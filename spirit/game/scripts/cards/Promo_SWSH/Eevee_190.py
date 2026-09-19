from spirit.game.scripts.cards.Promo_SWSH.Eevee_175 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=190,
    rarity=Rarities.RarePromo,
    guid='963b1432-7cf7-59fc-919d-d7cc66ce63e1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH190'}
