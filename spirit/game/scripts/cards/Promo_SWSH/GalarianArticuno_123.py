from spirit.game.scripts.cards.SWSH7.GalarianArticuno_63 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=123,
    rarity=Rarities.RarePromo,
    guid='78250640-e727-57d5-afd2-1181b9545da9',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH123'}
