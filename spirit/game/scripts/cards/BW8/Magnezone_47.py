from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.trainers import is_basic_energy_card

async def double_assist(ctx):
    """30. Attach 2 basic Energy cards from your discard pile to 1 of your
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
    guid="1107b031-fb45-54e6-9c6b-634b6140879e",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnezone.Name",
    display_name="Magnezone",
    searchable_by=["Magnezone","Stage 2","Magnezone"],
    subtypes=["Stage 2"],
    collector_number=47,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Magneton.Name",
    abilities=[
        Attack(
            title="Double Assist",
            game_text="Attach 2 basic Energy cards from your discard pile to 1 of your Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=double_assist,
        ),
        Attack(
            title="Tumbling Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
