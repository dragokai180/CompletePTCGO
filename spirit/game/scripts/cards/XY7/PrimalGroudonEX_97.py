from spirit.game.scripts.cards.XY5.PrimalGroudonEX_86 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities
from spirit.game.card_effects.standard_era import standard_passive


card = reprint(
    base_card,
    collector_number=97,
    rarity=Rarities.RareSecret,
    guid='74343277-b250-536b-aadf-d98d3b9a3d56',
    set_code='XY7',
    key='XY7',
    regulation_mark=None,
)

# Same attacks and stats, but this printing has theta Max, not omega Barrier.
card.passive = standard_passive(
    'When 1 of your Pokémon becomes this Pokémon, heal all damage from it.'
)
