from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


def _is_team_rockets(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Team Rocket's ")


def _power_saver_ok(board, player_id, pokemon=None) -> bool:
    return sum(1 for p in board.pokemon_in_play(player_id) if _is_team_rockets(p)) >= 4


async def erasure_ball(ctx):
    """160+. You may discard up to 2 Energy from your Benched Pokémon for +60 each."""
    energies = []
    for pokemon in ctx.my_bench():
        energies.extend(ctx.attached_energies(pokemon))
    discarded = 0
    if energies and await ctx.ask_yes_no(
        "Discard up to 2 Energy from your Benched Pokémon?"
    ):
        picks = await ctx.choose_cards(
            energies, 2, minimum=0,
            prompt="Choose up to 2 Energy to discard.",
        )
        if picks:
            await ctx.discard_cards(picks)
            discarded = len(picks)
    await ctx.deal_damage(160 + 60 * discarded)


card = PokemonCardDef(
    guid="3edec6e1-fa7f-5126-972e-d6e992feca39",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamRocketsMewtwoex.Name",
    display_name="Team Rocket's Mewtwo ex",
    searchable_by=["Team Rocket's Mewtwo ex", "Basic", "ex", "TeamRocketsMewtwoex"],
    subtypes=["Basic", "ex"],
    collector_number=81,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=280,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=150,
    abilities=[
        Ability(
            title="Power Saver",
            game_text="This Pokémon can't attack unless you have 4 or more Team Rocket's Pokémon in play.",
        ),
        Attack(
            title="Erasure Ball",
            game_text="You may discard up to 2 Energy from your Benched Pokémon. This attack does 60 more damage for each card you discarded in this way.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            damage_operator="+",
            condition=_power_saver_ok,
            effect=erasure_ball,
        ),
    ],
)
