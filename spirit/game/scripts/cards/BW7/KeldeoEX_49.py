from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

def rush_in_condition(board, player_id, pokemon):
    return pokemon is not board.active_pokemon(player_id)


async def rush_in(ctx):
    """Once during your turn (before your attack), if this Pokémon is on your
    Bench, you may switch this Pokémon with your Active Pokémon."""
    await ctx.switch_active(ctx.player_id, ctx.source)



card = PokemonCardDef(
    guid="733c9e38-34b2-55d4-b824-e552b9a950f1",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KeldeoEX.Name",
    display_name="Keldeo-EX",
    searchable_by=["Keldeo-EX","Basic","EX","KeldeoEX"],
    subtypes=["Basic","EX"],
    collector_number=49,
    set_code="BW7",
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Ability(
            title="Rush In",
            game_text="Once during your turn (before your attack), if this Pokémon is on your Bench, you may switch this Pokémon with your Active Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=rush_in_condition,
            effect=rush_in,
        ),
        Attack(
            title="Secret Sword",
            game_text="Does 20 more damage for each Water Energy attached to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
