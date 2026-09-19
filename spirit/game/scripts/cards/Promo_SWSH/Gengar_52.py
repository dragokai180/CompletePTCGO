from spirit.game.scripts.cards.SWSH1.Gengar_85 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=52,
    rarity=Rarities.RarePromo,
    guid='99738936-c6cc-58d2-86c0-4f996fa0650c',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH052'}
