from spirit.game.scripts.cards.SWSH6.Cinderace_28 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=112,
    rarity=Rarities.RarePromo,
    guid='a0227da0-3dbd-5078-8112-ade043e48495',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH112'}
