from spirit.game.scripts.cards.PGO.Bulbasaur_1 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=231,
    rarity=Rarities.RarePromo,
    guid='4bc7dd6f-c330-5eff-80ea-9a151534b824',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH231'}
