from spirit.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, subtypes_for,
)
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import search_to_hand, requires_bench_space


def _has_colorless_mega_ex(board, player_id, pokemon=None):
    if not requires_bench_space(1)(board, player_id):
        return False
    for p in board.pokemon_in_play(player_id):
        types = p.get_attribute(AttrID.POKEMON_TYPES) or []
        if (
            PokemonTypes.COLORLESS.value in types
            and "SV_Mega" in subtypes_for(p.archetype_id)
        ):
            return True
    return False


async def exciting_dive(ctx):
    """Put this Pokémon from your hand onto your Bench."""
    await ctx.bench_pokemon(ctx.source)


card = PokemonCardDef(
    guid="f3cf6934-554f-5274-a85a-c953fb488109",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Talonflameex.Name",
    display_name="Talonflame ex",
    searchable_by=["Talonflame ex","Stage 2","ex","Talonflameex"],
    subtypes=["Stage 2","ex"],
    collector_number=62,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Fletchinder.Name",
    family_id=661,
    abilities=[
        Ability(
            title="Exciting Dive",
            game_text="If this Pokémon is in your hand and you have any [C] Mega Evolution Pokémon ex in play, you may use this Ability. Put this Pokémon onto your Bench.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="hand",
            condition=_has_colorless_mega_ex,
            effect=exciting_dive,
        ),
        Attack(
            title="Talon Hunt",
            game_text="You may search your deck for up to 2 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=search_to_hand(count=2, minimum=0, reveal=False),
        ),
    ],
)
