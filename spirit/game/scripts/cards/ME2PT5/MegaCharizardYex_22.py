from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


async def explosion_y(ctx):
    """Discard 3 Energy from this Pokémon, and this attack does 280 damage
    to 1 of your opponent's Pokémon."""
    await ctx.discard_energy_from(
        ctx.attacker, 3,
        prompt="Choose 3 Energy to discard from this Pokémon",
    )
    await snipe_attack(280, pool="any")(ctx)


card = PokemonCardDef(
    guid="8498a04a-4e8a-5701-90dc-7d94d1e9babf",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaCharizardYex.Name",
    display_name="Mega Charizard Y ex",
    searchable_by=["Mega Charizard Y ex","Stage 2","ex","SV_Mega","MegaCharizardYex"],
    subtypes=["Stage 2","ex","SV_Mega"],
    collector_number=22,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=360,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    family_id=4,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    abilities=[
        Attack(
            title="Explosion Y",
            game_text="Discard 3 Energy from this Pokémon, and this attack does 280 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            effect=explosion_y,
        ),
    ],
)
