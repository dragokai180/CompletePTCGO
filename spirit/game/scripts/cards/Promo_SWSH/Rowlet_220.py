from spirit.game.scripts.cards.SWSH10.Rowlet_19 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=220,
    rarity=Rarities.RarePromo,
    guid='04eacbed-2bff-500c-8917-9ba4b787d230',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH220'}
