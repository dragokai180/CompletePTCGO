from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive
from spirit.game.models.board import BoardState


class _FestivalGroundsPassive(Passive):
    """Each Pokémon with any Energy attached can't be affected by Special
    Conditions (both sides)."""

    def blocks_special_conditions(self, target, condition, carrier):
        if target is None:
            return False
        return bool(BoardState.attached_energies(target))


card = StadiumCardDef(
    guid="5f24ff87-baf7-40c1-8975-fbcc0606e659",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.trainer.FestivalGrounds.Name",
    display_name="Festival Grounds",
    searchable_by=["Festival Grounds", "Stadium"],
    subtypes=["Stadium"],
    collector_number=149,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Uncommon,
    passive=_FestivalGroundsPassive(),
)

