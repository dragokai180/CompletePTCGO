from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def toppling_wind(ctx):
    """When you play this Pokémon from your hand to evolve 1 of your Pokémon,
    you may discard the top 3 cards of your opponent's deck."""
    if await ctx.ask_yes_no("Discard the top 3 cards of your opponent's deck?"):
        await ctx.discard_cards(ctx.deck_top(3, player_id=ctx.opponent_id))



card = PokemonCardDef(
    guid="4534801f-0b6a-5ac0-bd18-06d80d259b7b",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name",
    display_name="Aggron",
    searchable_by=["Aggron","Stage 2","Aggron"],
    subtypes=["Stage 2"],
    collector_number=80,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name",
    abilities=[
        Ability(
            title="Toppling Wind",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon, you may discard the top 3 cards of your opponent's deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=toppling_wind,
        ),
        Attack(
            title="Giga Horn",
            game_text="Flip 2 coins. If both of them are tails, this attack does nothing.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=bw_legacy_attack,
        ),
    ],
)
