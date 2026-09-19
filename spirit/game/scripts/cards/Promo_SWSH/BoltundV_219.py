from spirit.game.scripts.cards.SWSH8.BoltundV_103 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=219,
    rarity=Rarities.RarePromo,
    guid='d46da489-fec9-52d0-b85b-62e82469443d',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH219'}
