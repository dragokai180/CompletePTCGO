from spirit.game.scripts.cards.CZ.ZeraoraVSTAR_55 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=265,
    rarity=Rarities.RarePromo,
    guid='21e23991-7659-5fb4-bf63-3b70b9fd8fef',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH265'}
