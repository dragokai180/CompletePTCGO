from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_counters_on


async def whirling_envy(ctx):
    """20, +90 if this Pokemon has 2 or more damage counters. Damage isn't
    affected by Weakness."""
    bonus = 90 if damage_counters_on("self")(ctx) >= 2 else 0
    await ctx.deal_damage(20 + bonus, ignore_weakness=True)


card = PokemonCardDef(
    guid="e46a2813-d9b5-5529-a986-51c44ad9dd20",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYu.Name",
    display_name="Chi-Yu",
    searchable_by=["Chi-Yu","Basic","ChiYu"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=1004,
    abilities=[
        Attack(
            title="Whirling Envy",
            game_text="If this Pokémon has 2 or more damage counters on it, this attack does 90 more damage. This attack's damage isn't affected by Weakness.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=whirling_envy,
        ),
    ],
)
