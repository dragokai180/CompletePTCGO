from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities


def _has_ability(pokemon) -> bool:
    abilities = pokemon.get_attribute(AttrID.PIE_ABILITIES) or []
    return any(
        isinstance(entry, dict)
        and entry.get("abilityType") in ("PokeAbility", "PokePower")
        for entry in abilities
    )


async def law_of_the_underworld(ctx):
    """Put 6 damage counters on each Pokémon that has an Ability."""
    targets = [
        p for p in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play()
        if _has_ability(p)
    ]
    for target in targets:
        await ctx.deal_damage(
            60, target=target, apply_modifiers=False, as_counters=True,
        )


card = PokemonCardDef(
    guid="db778494-b15a-5458-94a0-2c7443ba40b9",
    key="SV08",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus","Stage 1","Cofagrigus"],
    subtypes=["Stage 1"],
    collector_number=83,
    set_code="SV08",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    family_id=562,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    abilities=[
        Attack(
            title="Law of the Underworld",
            game_text="Put 6 damage counters on each Pokémon that has an Ability (both yours and your opponent's).",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=law_of_the_underworld,
        ),
        Attack(
            title="Spooky Shot",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
        ),
    ],
)
