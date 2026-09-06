from spirit.game.data_utils import PokemonCardDef, Attack, Ability, is_pokemon_ex
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.passives_common import prevent_damage_when


def _mysterious_rock_inn(calc, carrier) -> bool:
    return (
        calc.target is carrier
        and calc.attacker is not None
        and is_pokemon_ex(calc.attacker.archetype_id)
    )


async def superb_scissors(ctx):
    """120. This attack's damage isn't affected by effects on the Active."""
    await ctx.deal_damage(ignore_target_effects=True)


card = PokemonCardDef(
    guid="14d06db4-8ba0-5436-907a-21f6fb2d2a8f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Crustle.Name",
    display_name="Crustle",
    searchable_by=["Crustle", "Stage 1", "Crustle"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dwebble.Name",
    family_id=557,
    abilities=[
        Ability(
            title="Mysterious Rock Inn",
            game_text="Prevent all damage done to this Pokémon by attacks from your opponent's Pokémon ex.",
            passive=prevent_damage_when(_mysterious_rock_inn),
        ),
        Attack(
            title="Superb Scissors",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=superb_scissors,
        ),
    ],
)
