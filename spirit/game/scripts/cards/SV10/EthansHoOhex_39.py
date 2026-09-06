from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.support_common import heal_targets
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_ethans(pokemon) -> bool:
    definition = def_for(pokemon.archetype_id)
    name = getattr(definition, "display_name", "") or ""
    return name.startswith("Ethan's ")


def _is_basic_fire_energy(card) -> bool:
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIRE.value
    )


def _golden_flame_condition(board, player_id, pokemon) -> bool:
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(_is_basic_fire_energy(c) for c in hand.children):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(_is_ethans(p) for p in bench.children)


async def golden_flame(ctx):
    """Once per turn: attach up to 2 Basic Fire Energy from hand to 1
    Benched Ethan's Pokémon."""
    energies = [c for c in ctx.hand() if _is_basic_fire_energy(c)]
    targets = [p for p in ctx.my_bench() if _is_ethans(p)]
    if not energies or not targets:
        return
    picks = await ctx.choose_cards(
        energies, 2, minimum=1,
        prompt="Choose up to 2 Basic Fire Energy cards to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(
        targets, "Choose your Benched Ethan's Pokémon"
    )
    if target is None:
        return
    for energy in picks:
        await ctx.attach_energy(energy, target)


card = PokemonCardDef(
    guid="d62d512a-018d-5364-9feb-d1d4166412e2",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansHoOhex.Name",
    display_name="Ethan's Ho-Oh ex",
    searchable_by=["Ethan's Ho-Oh ex","Basic","ex","EthansHoOhex"],
    subtypes=["Basic","ex"],
    collector_number=39,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=230,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=250,
    abilities=[
        Ability(
            title="Golden Flame",
            game_text="Once during your turn, you may attach up to 2 Basic Fire Energy cards from your hand to 1 of your Benched Ethan's Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_golden_flame_condition,
            effect=golden_flame,
        ),
        Attack(
            title="Shining Feathers",
            game_text="Heal 50 damage from each of your Pokémon.",
            cost={PokemonTypes.FIRE: 4},
            damage=160,
            effect=heal_targets(50, "each_own"),
        ),
    ],
)
