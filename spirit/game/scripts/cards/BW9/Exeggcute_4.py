from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


async def propagation(ctx):
    """Once per turn, from the discard pile: you may put this Pokemon into
    your hand. The discard pile is public, so nothing needs revealing."""
    if not await ctx.ask_yes_no("Put this Pokemon into your hand?"):
        return
    await ctx.put_in_hand([ctx.source], reveal=False)


card = PokemonCardDef(
    guid="5539136b-dc3d-5c73-a2b5-a7ca95f8b8e7",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic", "Exeggcute"],
    subtypes=["Basic"],
    collector_number=4,
    set_code="BW9",
    rarity=Rarities.Uncommon,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=102,
    abilities=[
        Ability(
            title="Propagation",
            game_text="Once during your turn (before your attack), if this Pokémon is in your discard pile, you may put this Pokémon into your hand.",
            usable_from="discard",
            activation=Activations.ONCE_PER_TURN,
            effect=propagation,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
