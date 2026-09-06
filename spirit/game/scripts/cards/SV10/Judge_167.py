from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.trainers import judge


card = SupporterCardDef(
    guid="2059bbd1-a999-530e-a661-9296d85ddee7",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Judge.Name",
    display_name="Judge",
    searchable_by=["Judge", "Supporter", "Judge"],
    subtypes=["Supporter"],
    collector_number=167,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=judge,
)
