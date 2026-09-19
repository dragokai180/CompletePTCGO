from spirit.game.scripts.cards.SWSH1.CramorantV_155 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=86,
    rarity=Rarities.RarePromo,
    guid='aba91cda-e801-59de-bf6c-15f46ba3f1dc',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH086'}
