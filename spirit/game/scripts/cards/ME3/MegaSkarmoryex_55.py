from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import snipe_attack


async def sonic_ripper(ctx):
    """Shuffle all Energy attached to this Pokémon into your deck, and this
    attack does 220 damage to 1 of your opponent's Pokémon. (Don't apply
    Weakness and Resistance for Benched Pokémon.)"""
    energies = list(ctx.attached_energies(ctx.attacker))
    if energies:
        await ctx.shuffle_into_deck(energies, player_id=ctx.player_id)
    await snipe_attack(220, pool="any")(ctx)


card = PokemonCardDef(
    guid="d42d31e2-9ffb-5846-8f94-addad768bc36",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaSkarmoryex.Name",
    display_name="Mega Skarmory ex",
    searchable_by=["Mega Skarmory ex", "Basic", "ex", "SV_Mega", "MegaSkarmoryex"],
    subtypes=["Basic", "ex", "SV_Mega"],
    collector_number=55,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=227,
    abilities=[
        Attack(
            title="Sonic Ripper",
            game_text="Shuffle all Energy attached to this Pokémon into your deck, and this attack does 220 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            effect=sonic_ripper,
        ),
    ],
)
