from spirit.game.data_utils import SupporterCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.session.passives import effective_max_hp


def _is_psychic_pokemon(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.PSYCHIC.value in types


def _is_damaged(board, pokemon):
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


def _jacinthe_condition(board, player_id):
    return any(
        _is_psychic_pokemon(p) and _is_damaged(board, p)
        for p in board.pokemon_in_play(player_id)
    )


async def jacinthe(ctx):
    """Heal 150 damage from 1 of your Psychic Pokémon."""
    eligible = [
        p for p in ctx.my_pokemon_in_play()
        if _is_psychic_pokemon(p) and _is_damaged(ctx.board, p)
    ]
    if not eligible:
        return
    target = await ctx.choose_pokemon(eligible, "Choose a Psychic Pokémon to heal")
    if target is not None:
        await ctx.heal(150, target)


card = SupporterCardDef(
    guid="22fed7a7-bd29-5a06-a06b-b30799ee0d93",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.trainer.Jacinthe.Name",
    display_name="Jacinthe",
    searchable_by=["Jacinthe", "Supporter", "Jacinthe"],
    subtypes=["Supporter"],
    collector_number=75,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    effect=jacinthe,
    condition=_jacinthe_condition,
)
