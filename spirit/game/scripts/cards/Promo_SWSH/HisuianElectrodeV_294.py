from spirit.game.scripts.cards.SWSH11.HisuianElectrodeV_172 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=294,
    rarity=Rarities.RarePromo,
    guid='53341aae-e2cc-59ed-a224-a8049264ebaa',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='F',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH294'}
