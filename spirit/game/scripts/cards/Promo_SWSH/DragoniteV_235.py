from spirit.game.scripts.cards.PGO.DragoniteV_49 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=235,
    rarity=Rarities.RarePromo,
    guid='18b657ee-9740-5283-8274-43b360b84039',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH235'}
