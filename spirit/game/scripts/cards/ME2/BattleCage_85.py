from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, Rarities
from spirit.game.session.passives import Passive


class BattleCagePassive(Passive):
    """Prevent damage counters on Benched Pokémon from opposing Pokémon
    attacks and Abilities. Attack damage is still taken."""

    def blocks_damage_counters(self, target, carrier):
        parent = target.parent
        return bool(parent) and parent.get_attribute(AttrID.NAME) == "bench"


card = StadiumCardDef(
    guid="49c7c057-4346-59ab-a04d-2ee13a2834bd",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.BattleCage.Name",
    display_name="Battle Cage",
    searchable_by=["Battle Cage", "Stadium", "BattleCage"],
    subtypes=["Stadium"],
    collector_number=85,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    passive=BattleCagePassive(),
)
