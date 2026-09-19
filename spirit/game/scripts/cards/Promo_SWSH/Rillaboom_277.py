from spirit.game.scripts.cards.SWSH6.Rillaboom_18 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=277,
    rarity=Rarities.RarePromo,
    guid='e368f535-8758-5b0c-a90d-35fca7ff19c1',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH277'}
