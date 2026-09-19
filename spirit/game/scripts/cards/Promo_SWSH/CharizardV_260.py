from spirit.game.scripts.cards.SWSH9.CharizardV_17 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=260,
    rarity=Rarities.RarePromo,
    guid='c3362940-2916-5794-8426-9971ea8eb93d',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH260'}
