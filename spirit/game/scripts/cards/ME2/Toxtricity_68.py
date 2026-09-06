from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card, is_darkness_pokemon


def _is_basic_darkness_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.DARKNESS.value
    )


def _sinister_surge_condition(board, player_id, pokemon=None):
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(is_darkness_pokemon(p) for p in bench.children)


async def sinister_surge(ctx):
    """Once during your turn, you may use this Ability. Search your deck for a
    Basic Darkness Energy card and attach it to 1 of your Benched Darkness
    Pokémon. Then, shuffle your deck. If you attached Energy to a Pokémon in
    this way, place 2 damage counters on that Pokémon."""
    if not await ctx.ask_yes_no(
        "Search your deck for a Basic Darkness Energy card and attach it to "
        "1 of your Benched Darkness Pokémon?"
    ):
        return
    picks = await ctx.search_deck(
        _is_basic_darkness_energy, count=1, minimum=0,
        prompt="Choose a Basic Darkness Energy card to attach.",
    )
    if picks:
        candidates = [p for p in ctx.my_bench() if is_darkness_pokemon(p)]
        if candidates:
            target = await ctx.choose_pokemon(
                candidates, "Choose a Benched Darkness Pokémon to attach the Energy to"
            )
            if target is not None:
                await ctx.attach_energy(picks[0], target)
                await ctx.deal_damage(
                    20, target=target, apply_modifiers=False, as_counters=True
                )
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="2a577aee-d427-55bf-bb61-0a841a765f76",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxtricity.Name",
    display_name="Toxtricity",
    searchable_by=["Toxtricity", "Stage 1", "Toxtricity"],
    subtypes=["Stage 1"],
    collector_number=68,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Toxel.Name",
    family_id=848,
    abilities=[
        Ability(
            title="Sinister Surge",
            game_text="Once during your turn, you may use this Ability. Search your deck for a Basic Darkness Energy card and attach it to 1 of your Benched Darkness Pokémon. Then, shuffle your deck. If you attached Energy to a Pokémon in this way, place 2 damage counters on that Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            effect=sinister_surge,
            condition=_sinister_surge_condition,
        ),
        Attack(
            title="Gentle Slap",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
