# Gallery print swsh12tg/TG26; artwork is downloaded by the installer.
from spirit.game.card_effects.galleries import professor_burnet
from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import deck_nonempty


card = SupporterCardDef(
    guid='55dd9ea6-f7ae-5705-9063-e5db2acc1ae6',
    key='SWSH12',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ProfessorBurnet.Name',
    display_name='Professor Burnet',
    searchable_by=['Professor Burnet', 'Supporter', 'ProfessorBurnet'],
    subtypes=['Supporter'],
    collector_number=241,
    set_code='SWSH12',
    regulation_mark='E',
    rarity=Rarities.RareUltra,
    attributes={200790: {'type': 'string', 'value': 'TG26'}},
    effect=professor_burnet,
    condition=deck_nonempty,
)

card.extra_attributes["200790"] = {"type": "string", "value": "TG26"}
