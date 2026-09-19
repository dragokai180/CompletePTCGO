from spirit.game.scripts.cards.Promo_SWSH.Eevee_175 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=212,
    rarity=Rarities.RarePromo,
    guid='08463e1d-9030-503f-a350-760a85af87dc',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='E',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH212'}
