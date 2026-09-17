from spirit.game.scripts.cards.ME55.Mew_65 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=160,
    rarity=Rarities.Common,
    guid='eeaf692c-2af4-56fd-8ffd-da47e23c805c',
    set_code='ME55',
    key='ME55',
    regulation_mark='J',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'G'}
