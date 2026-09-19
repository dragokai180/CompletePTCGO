from spirit.game.scripts.cards.SWSH5.Cherrim_8 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=88,
    rarity=Rarities.RarePromo,
    guid='84d0270c-9596-5cb9-97b0-fcfc602b7784',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH088'}
