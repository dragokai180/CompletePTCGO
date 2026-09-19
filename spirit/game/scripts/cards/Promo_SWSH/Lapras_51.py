from spirit.game.scripts.cards.SWSH1.Lapras_48 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=51,
    rarity=Rarities.RarePromo,
    guid='efdea338-2e98-57a0-877b-7a80bc18f366',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH051'}
