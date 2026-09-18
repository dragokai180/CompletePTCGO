from spirit.game.scripts.cards.XY5.PrimalKyogreEX_55 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities
from spirit.game.card_effects.standard_era import standard_passive


card = reprint(
    base_card,
    collector_number=96,
    rarity=Rarities.RareSecret,
    guid='40efb67e-0b9d-544c-a294-2304cae88e5a',
    set_code='XY7',
    key='XY7',
    regulation_mark=None,
)

# Same attacks and stats, but this printing has theta Max, not alpha Growth.
card.passive = standard_passive(
    'When 1 of your Pokémon becomes this Pokémon, heal all damage from it.'
)
