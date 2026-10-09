from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import Rarities
from spirit.game.session.passives import Passive
from spirit.game.models.board import BoardState
from spirit.game.card_effects.pokemon import recover_from_festival_grounds


class _FestivalGroundsPassive(Passive):
    """Each Pokémon with Energy attached can't gain Special Conditions."""

    def blocks_special_conditions(self, target, condition, carrier):
        if target is None:
            return False
        return bool(BoardState.attached_energies(target))


async def festival_grounds_effect(ctx):
    """The Stadium also removes existing conditions when it enters play."""
    for pokemon in (*ctx.my_pokemon_in_play(), *ctx.opponent_pokemon_in_play()):
        await recover_from_festival_grounds(ctx, pokemon)


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
    effect=festival_grounds_effect,
)

