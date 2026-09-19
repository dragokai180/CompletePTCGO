from spirit.game.scripts.cards.BW1.PokBall_97 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=146,
    rarity=Rarities.RarePromo,
    guid='fb1c3347-3439-5258-9643-d89cfe096295',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH146'}
