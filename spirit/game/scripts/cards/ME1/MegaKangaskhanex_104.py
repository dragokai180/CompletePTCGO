from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import in_active_spot


async def run_errand(ctx):
    """Once during your turn, if this Pokémon is in the Active Spot, you may
    use this Ability. Draw 2 cards. You can't use more than 1 Run Errand
    Ability each turn."""
    await ctx.draw_cards(2)


card = PokemonCardDef(
    guid="60a41840-4a64-558a-b857-a8d6de234508",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaKangaskhanex.Name",
    display_name="Mega Kangaskhan ex",
    searchable_by=["Mega Kangaskhan ex","Basic","ex","SV_Mega","MegaKangaskhanex"],
    subtypes=["Basic","ex","SV_Mega"],
    collector_number=104,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=300,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=115,
    abilities=[
        Ability(
            title="Run Errand",
            game_text="Once during your turn, if this Pokémon is in the Active Spot, you may use this Ability. Draw 2 cards. You can't use more than 1 Run Errand Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Run Errand",
            condition=in_active_spot,
            effect=run_errand,
        ),
        Attack(
            title="Rapid-Fire Combo",
            game_text="Flip a coin until you get tails. This attack does 50 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=200,
            damage_operator="+",
            effect=flip_damage(until_tails=True, bonus_per_heads=50),
        ),
    ],
)
