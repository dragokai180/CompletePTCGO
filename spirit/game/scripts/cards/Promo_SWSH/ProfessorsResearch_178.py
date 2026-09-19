from spirit.game.scripts.cards.CEL25.ProfessorsResearchProfessorOak_23 import card as base_card
from spirit.game.data_utils import reprint
from spirit.game.attributes import Rarities


card = reprint(
    base_card,
    collector_number=178,
    rarity=Rarities.RarePromo,
    guid='717bc92e-1f9c-52fb-823f-199c42575cd9',
    set_code='Promo_SWSH',
    key='Promo_SWSH',
    regulation_mark='D',
)

card.extra_attributes['200790'] = {'type': 'string', 'value': 'SWSH178'}
