from spirit.game.scripts.cards.PROMO_BW.ChampionsFestival_BW95 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=296,
    rarity=Rarities.RarePromo,
    guid='669be36d-a50e-53bc-a76a-cdd035e9b8c3',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH296'}
