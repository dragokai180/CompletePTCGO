from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import distribute_energy
from spirit.game.card_effects.trainers import is_basic_energy_card


async def turbo_flare(ctx):
    """50. Search your deck for up to 3 Basic Energy cards and attach them
    to your Benched Pokémon in any way you like."""
    await ctx.deal_damage()
    bench = ctx.my_bench()
    if not bench:
        return
    picks = await ctx.search_deck(
        is_basic_energy_card, count=3, minimum=0,
        prompt="Choose up to 3 Basic Energy cards to attach to your Benched Pokémon.",
    )
    if picks:
        await distribute_energy(ctx, picks, bench)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="26a1b82c-0bad-5dd6-851e-74da804647b5",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cinderace.Name",
    display_name="Cinderace",
    searchable_by=["Cinderace","Stage 2","Cinderace"],
    subtypes=["Stage 2"],
    collector_number=28,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    family_id=813,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Raboot.Name",
    setup_as_active=True,
    abilities=[
        Ability(
            title="Explosiveness",
            game_text="If this Pokémon is in your hand when you are setting up to play, you may put it face down in the Active Spot.",
        ),
        Attack(
            title="Turbo Flare",
            game_text="Search your deck for up to 3 Basic Energy cards and attach them to your Benched Pokémon in any way you like. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=turbo_flare,
        ),
    ],
)
