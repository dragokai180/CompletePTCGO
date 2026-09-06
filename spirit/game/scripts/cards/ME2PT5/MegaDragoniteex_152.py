from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.trainers import player_has_bench


def _has_bench(board, player_id, pokemon=None):
    return player_has_bench(board, player_id)


async def sky_transport(ctx):
    """Switch your Active Pokémon with 1 of your Benched Pokémon."""
    target = await ctx.choose_pokemon(
        ctx.my_bench(), "Choose your new Active Pokémon"
    )
    if target is not None:
        await ctx.switch_active(ctx.player_id, target)


card = PokemonCardDef(
    guid="ea5b4a91-0c51-5f16-a8d4-bd044c1a175d",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaDragoniteex.Name",
    display_name="Mega Dragonite ex",
    searchable_by=["Mega Dragonite ex","Stage 2","ex","SV_Mega","MegaDragoniteex"],
    subtypes=["Stage 2","ex","SV_Mega"],
    collector_number=152,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=370,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    family_id=147,
    abilities=[
        Ability(
            title="Sky Transport",
            game_text="Once during your turn, you may use this Ability. Switch your Active Pokémon with 1 of your Benched Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_has_bench,
            effect=sky_transport,
        ),
        Attack(
            title="Ryuno Glide",
            game_text="Discard 2 Energy from this Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 2},
            damage=330,
            effect=self_energy_discard_attack(count=2),
        ),
    ],
)
