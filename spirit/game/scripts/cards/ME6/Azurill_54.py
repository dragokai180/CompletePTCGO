from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_energy_card


async def hopping_charge(ctx):
    """Search your deck for an Energy card and attach it to 1 of your Benched
    Pokémon. Then, shuffle your deck."""
    picks = await ctx.search_deck(
        is_energy_card, count=1, minimum=0,
        prompt="Choose an Energy card to attach.",
    )
    if picks:
        bench = ctx.my_bench()
        if bench:
            target = await ctx.choose_pokemon(
                bench, "Choose a Benched Pokémon to attach the Energy to"
            )
            if target is not None:
                await ctx.attach_energy(picks[0], target)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="275fe0a3-554f-54a7-ae99-37dcf1e0a922",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azurill.Name",
    display_name="Azurill",
    searchable_by=["Azurill","Basic","Azurill"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=298,
    abilities=[
        Attack(
            title="Hopping Charge",
            game_text="Search your deck for an Energy card and attach it to 1 of your Benched Pokémon. Then, shuffle your deck.",
            cost={},
            effect=hopping_charge,
        ),
    ],
)
