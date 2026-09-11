from spirit.game.data_utils import StadiumCardDef
from spirit.game.attributes import AttrID, Rarities, SpecialConditions
from spirit.game.session.passives import Passive


_SLEEP_SIDE_CONDITIONS = {
    SpecialConditions.ASLEEP,
    SpecialConditions.PARALYZED,
}
_CONFUSION_SIDE_CONDITIONS = {
    SpecialConditions.CONFUSED,
    SpecialConditions.POISONED,
}


def _other_player(carrier):
    playmat = carrier.parent.parent if carrier.parent else None
    return next(
        (
            child.owning_player_id for child in (playmat.children if playmat else [])
            if child.owning_player_id
            and child.owning_player_id != carrier.owning_player_id
        ),
        None,
    )


def _sleep_side(carrier):
    return _other_player(carrier) \
        if carrier.get_attribute(AttrID.CARD_ORIENTATION, 0) == 1 \
        else carrier.owning_player_id


def protected_conditions(carrier, player_id):
    return _SLEEP_SIDE_CONDITIONS \
        if player_id == _sleep_side(carrier) \
        else _CONFUSION_SIDE_CONDITIONS


class ChaosTowerPassive(Passive):
    def blocks_special_conditions(self, target, condition, carrier):
        return condition in protected_conditions(
            carrier, target.owning_player_id
        )


async def chaos_tower(ctx):
    """Immediately clear the conditions forbidden by the chosen side."""
    for player_id in (ctx.player_id, ctx.opponent_id):
        forbidden = protected_conditions(ctx.source, player_id)
        for pokemon in ctx.board.pokemon_in_play(player_id):
            for condition in forbidden:
                await ctx.cure_condition(pokemon, condition)


card = StadiumCardDef(
    guid='b261ac6f-3f12-5fb5-ac4d-21f93dfe979d',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.trainer.ChaosTower.Name',
    display_name='Chaos Tower',
    searchable_by=['Chaos Tower', 'Stadium', 'ChaosTower'],
    subtypes=['Stadium'],
    collector_number=94,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    effect=chaos_tower,
    passive=ChaosTowerPassive(),
    orientation_choices=[
        (
            "Orientação normal",
            "Seus Pokémon não podem ficar Adormecidos ou Paralisados; os adversários não podem ficar Confusos ou Envenenados.",
        ),
        (
            "Orientação invertida",
            "Seus Pokémon não podem ficar Confusos ou Envenenados; os adversários não podem ficar Adormecidos ou Paralisados.",
        ),
    ],
    allows_same_name_replacement=True,
)
