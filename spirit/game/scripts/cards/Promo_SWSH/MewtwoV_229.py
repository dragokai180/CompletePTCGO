from spirit.game.scripts.cards.PGO.MewtwoV_30 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=229,
    rarity=Rarities.RarePromo,
    guid='657a82ff-fb27-5901-be42-e3083b21c595',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH229'}
