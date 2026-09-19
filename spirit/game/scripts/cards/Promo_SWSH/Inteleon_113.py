from spirit.game.scripts.cards.SWSH6.Inteleon_43 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=113,
    rarity=Rarities.RarePromo,
    guid='36b82f8a-ab68-56ff-8611-3a7de7b407f7',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH113'}
