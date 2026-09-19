from spirit.game.scripts.cards.SWSH6.Cinderace_28 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=278,
    rarity=Rarities.RarePromo,
    guid='af20d970-306f-51ee-9e26-9a1cf9900b23',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH278'}
