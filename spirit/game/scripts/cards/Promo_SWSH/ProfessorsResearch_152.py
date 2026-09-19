from spirit.game.scripts.cards.CEL25.ProfessorsResearchProfessorOak_23 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=152,
    rarity=Rarities.RarePromo,
    guid='c0876ac0-5f07-5fcd-8973-cae34a72bf12',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH152'}
