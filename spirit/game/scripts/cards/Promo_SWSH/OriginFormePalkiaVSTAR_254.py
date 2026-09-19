from spirit.game.scripts.cards.SWSH10.OriginFormePalkiaVSTAR_40 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=254,
    rarity=Rarities.RarePromo,
    guid='28bb8aec-8798-520e-ae17-c59fd15b928f',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH254'}
