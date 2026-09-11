from spirit.game.scripts.cards.Promo_SM.Pikachu_98 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=40,
    rarity=Rarities.Common,
    guid='42d5becf-c475-5832-8ddc-114fec26ea8d',
    set_code='SM3',
    key='SM3',
    regulation_mark=None,
)
