from spirit.game.scripts.cards.SWSH10.Oshawott_41 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=222,
    rarity=Rarities.RarePromo,
    guid='3945cd19-c025-5698-bc84-bf85404fafe4',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH222'}
