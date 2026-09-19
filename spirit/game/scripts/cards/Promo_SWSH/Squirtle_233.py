from spirit.game.scripts.cards.PGO.Squirtle_15 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=233,
    rarity=Rarities.RarePromo,
    guid='efcca270-b213-5271-a92e-a74575a3e012',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH233'}
