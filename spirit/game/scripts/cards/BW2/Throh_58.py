from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import lock_defender_attacks

async def scarf_hold(ctx):
    heads = await ctx.flip_coins(1, "Entangling String")
    if heads[0]:
        lock_defender_attacks(ctx)


card = PokemonCardDef(
    guid="777375ba-8f32-5a14-9985-7eb1309eb1b0",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh","Basic","Throh"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Scarf Hold",
            game_text="Flip a coin. If heads, the Defending Pokémon can't attack during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=scarf_hold,
        ),
    ],
)
