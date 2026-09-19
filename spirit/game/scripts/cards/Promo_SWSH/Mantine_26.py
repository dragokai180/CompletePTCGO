from spirit.game.scripts.cards.SWSH1.Mantine_52 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=26,
    rarity=Rarities.RarePromo,
    guid='72bd632f-8b43-54ed-ac5f-52ec5ca43019',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH026'}
