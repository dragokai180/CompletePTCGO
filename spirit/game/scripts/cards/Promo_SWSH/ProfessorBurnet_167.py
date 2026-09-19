from spirit.game.scripts.cards.SWSH12.ProfessorBurnet_241 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=167,
    rarity=Rarities.RarePromo,
    guid='ca7f76f6-42da-57c2-9ebe-fd3cd7323726',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH167'}
