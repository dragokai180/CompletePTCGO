from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import Rarities
from spirit.game.card_effects.support_common import heal_targets, requires_damaged_pokemon

card = SupporterCardDef(
    guid="a78c6e8c-107c-5b54-b53c-659d26dbb735",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Fennel.Name",
    display_name="Fennel",
    searchable_by=["Fennel","Supporter","Fennel"],
    subtypes=["Supporter"],
    collector_number=82,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=heal_targets(40, scope="each_own"),
    condition=requires_damaged_pokemon(),
)
