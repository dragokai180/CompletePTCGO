from spirit.game.scripts.cards.SWSH6.Inteleon_43 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=279,
    rarity=Rarities.RarePromo,
    guid='a6777264-01da-5f5e-ac99-c37211401c1f',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH279'}
