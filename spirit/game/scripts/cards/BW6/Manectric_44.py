from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.trainers import is_basic_energy_card

async def energy_assist(ctx):
    """Attach 2 basic Energy cards from your discard pile to 1 of your Benched
    Pokémon."""
    await ctx.deal_damage()
    cards = [c for c in ctx.discard_pile() if is_basic_energy_card(c)]
    bench = ctx.my_bench()
    if not cards or not bench:
        return
    picks = await ctx.choose_cards(
        cards, 2, minimum=1,
        prompt="Choose up to 2 basic Energy cards from your discard pile to attach",
    )
    if not picks:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon") or bench[0]
    for card in picks:
        await ctx.attach_energy(card, target)



card = PokemonCardDef(
    guid="dd240697-6439-5aa4-af56-5ab8ee581fc2",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric","Stage 1","Manectric"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    abilities=[
        Attack(
            title="Energy Assist",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Benched Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=energy_assist,
        ),
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
