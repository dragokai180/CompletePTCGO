from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.bw10 import freestyle_strike, shoulder_throw
from spirit.game.card_effects.trainers import is_basic_energy_card

async def gather_energy(ctx):
    """30. Search your deck for a basic Energy card and attach it to 1 of your
    Pokémon. Shuffle your deck afterward."""
    picks = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=0,
        prompt="Choose a basic Energy card to attach.",
    )
    await ctx.shuffle_deck()
    if not picks:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)



card = PokemonCardDef(
    guid="e7cf9a54-d2d3-51d2-80c1-1cb1574b2af1",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Delcatty.Name",
    display_name="Delcatty",
    searchable_by=["Delcatty","Stage 1","Delcatty"],
    subtypes=["Stage 1"],
    collector_number=114,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name",
    abilities=[
        Attack(
            title="Gather Energy",
            game_text="Search your deck for a basic Energy card and attach it to 1 of your Pokémon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=gather_energy,
        ),
        Attack(
            title="Double Slap",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="x",
            effect=freestyle_strike,
        ),
    ],
)
