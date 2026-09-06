from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID


def _pokemon_has_any_ability(pokemon) -> bool:
    """Printed abilities include both Ability(passive) and Attack entries.
    We only care about non-Attack abilities for 'has an Ability' text."""
    for entry in pokemon.get_attribute(AttrID.PIE_ABILITIES) or []:
        if not isinstance(entry, dict):
            continue
        if entry.get("abilityType") == "Attack":
            continue
        return True
    return False


async def freezing_shroud(ctx):
    """During Pokemon Checkup: put 1 damage counter on each Pokémon that has
    an Ability (both yours and your opponent's), except any Froslass."""
    for pokemon in ctx.my_pokemon_in_play() + ctx.opponent_pokemon_in_play():
        if (
            pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Froslass"
        ):
            continue
        if not _pokemon_has_any_ability(pokemon):
            continue
        await ctx.deal_damage(10, target=pokemon, as_counters=True, is_attack=False)


card = PokemonCardDef(
    guid="116e0c22-1b5f-431e-b7b9-9d0ef3fa4482",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froslass.Name",
    display_name="Froslass",
    searchable_by=["Froslass", "Stage 1", "Froslass"],
    subtypes=["Stage 1"],
    collector_number=53,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=361,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name",
    abilities=[
        Ability(
            title="Freezing Shroud",
            game_text=(
                "During Pokémon Checkup, put 1 damage counter on each Pokémon "
                "that has an Ability (both yours and your opponent's), "
                "except any Froslass."
            ),
            trigger=Triggers.BETWEEN_TURNS,
            effect=freezing_shroud,
        ),
        Attack(
            title="Frost Smash",
            game_text="",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)

