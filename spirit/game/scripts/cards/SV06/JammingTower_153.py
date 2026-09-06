from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive


class _JammingTowerPassive(Passive):
    """Pokemon Tools attached to each Pokémon have no effect."""

    def suppresses_tool(self, tool, carrier):
        return True


card = StadiumCardDef(
    guid="d9e38c83-c1de-47e5-b288-f3509aa1f06e",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.JammingTower.Name",
    display_name="Jamming Tower",
    searchable_by=["Jamming Tower", "Stadium"],
    subtypes=["Stadium"],
    collector_number=153,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=_JammingTowerPassive(),
)

