from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.pokemon import TeraRulePassive


async def moss_agate(ctx):
    """230. Heal 100 damage from each of your Benched Pokémon."""
    await ctx.deal_damage()
    for pokemon in ctx.my_bench():
        await ctx.heal(100, pokemon)


card = PokemonCardDef(
    guid="e85ec9b5-2407-575d-8e02-a451816df6b1",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Leafeonex.Name",
    display_name="Leafeon ex",
    searchable_by=["Leafeon ex","Stage 1","ex","Tera","Leafeonex"],
    subtypes=["Stage 1","ex","Tera"],
    collector_number=6,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Verdant Storm",
            game_text="This attack does 60 damage for each Energy attached to all of your opponent's Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="x",
            effect=damage_per(count_energy("opponent"), 60),
        ),
        Attack(
            title="Moss Agate",
            game_text="Heal 100 damage from each of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1},
            damage=230,
            effect=moss_agate,
        ),
    ],
)
