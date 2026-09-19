from spirit.game.scripts.cards.Promo_SWSH.PikachuV_143 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=145,
    rarity=Rarities.RarePromo,
    guid='a5dab36c-1914-5a84-af1d-6bf39c581258',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH145'}
