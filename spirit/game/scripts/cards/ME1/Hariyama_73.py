from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


async def heave_ho_catcher(ctx):
    """Once during your turn, when you play this Pokémon from your hand to
    evolve 1 of your Pokémon, you may use this Ability. Switch in 1 of your
    opponent's Benched Pokémon to the Active Spot."""
    bench = ctx.opponent_bench()
    if not bench:
        return
    if not await ctx.ask_yes_no(
            "Switch in 1 of your opponent's Benched Pokémon to the Active Spot?"):
        return
    target = await ctx.choose_pokemon(
        bench, "Choose the opponent's new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.opponent_id, target)

card = PokemonCardDef(
    guid="1bcab814-7a45-5421-b692-de7f17cb5e6c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama","Stage 1","Hariyama"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Ability(
            title="Heave-Ho Catcher",
            game_text="Once during your turn, when you play this Pokémon from your hand to evolve 1 of your Pokémon, you may use this Ability. Switch in 1 of your opponent's Benched Pokémon to the Active Spot.",
            trigger=Triggers.ON_EVOLVE,
            effect=heave_ho_catcher,
        ),
        Attack(
            title="Wild Press",
            game_text="This Pokémon also does 70 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=210,
            effect=recoil_attack(70),
        ),
    ],
)
