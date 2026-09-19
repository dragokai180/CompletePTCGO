from spirit.game.scripts.cards.SWSH3.CharizardV_19 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=50,
    rarity=Rarities.RarePromo,
    guid='a6410d28-866c-5a69-b2bd-e292288e4b84',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH050'}
