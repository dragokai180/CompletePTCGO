from spirit.game.scripts.cards.SWSH7.Flaaffy_55 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=122,
    rarity=Rarities.RarePromo,
    guid='52a3f04b-c4c2-51d7-bcad-0ad1cabd97c0',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH122'}
