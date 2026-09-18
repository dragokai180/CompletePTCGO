from spirit.game.scripts.cards.XY6.MRayquazaEX_76 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities
from spirit.game.card_effects.standard_era import standard_passive


card = reprint(
    base_card,
    collector_number=98,
    rarity=Rarities.RareSecret,
    guid='8b393177-5104-5466-b5f5-984026936a0c',
    set_code='XY7',
    key='XY7',
    regulation_mark=None,
)

# Same attacks and stats, but this printing has theta Max, not delta Evolution.
card.passive = standard_passive(
    'When 1 of your Pokémon becomes this Pokémon, heal all damage from it.'
)
