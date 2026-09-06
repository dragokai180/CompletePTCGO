from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import recoil_attack


async def _paralyze_and_poison(ctx):
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.PARALYZED)
    await ctx.apply_special_condition(ctx.defender, SpecialConditions.POISONED)


card = PokemonCardDef(
    guid="9391b3d0-ef32-5b9e-ac58-551bedc9032a",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drapion.Name",
    display_name="Drapion",
    searchable_by=["Drapion","Stage 1","Drapion"],
    subtypes=["Stage 1"],
    collector_number=52,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    family_id=451,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name",
    abilities=[
        Attack(
            title="Wrack Down",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
        ),
        Attack(
            title="Hazardous Tail",
            game_text="This Pokémon also does 70 damage to itself. Your opponent's Active Pokémon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=100,
            effect=recoil_attack(70, also=_paralyze_and_poison),
        ),
    ],
)
