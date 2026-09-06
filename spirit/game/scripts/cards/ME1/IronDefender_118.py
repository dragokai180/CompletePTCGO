from spirit.game.data_utils import ItemCardDef
from spirit.game.attributes import AttrID, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import takes_less_passive


def _is_metal_teammate(target, carrier):
    if target.owning_player_id != carrier.owning_player_id:
        return False
    types = target.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.METAL.value in types


async def iron_defender(ctx):
    """During your opponent's next turn, all of your Metal Pokémon take 30
    less damage from attacks (including new Pokémon that come into play)."""
    shield = takes_less_passive(
        30, protects=_is_metal_teammate, stack_key="Iron Defender",
    )
    for pokemon in ctx.my_pokemon_in_play():
        ctx.add_passive_through_opponents_turn(pokemon, shield)


card = ItemCardDef(
    guid="ad66af6d-0758-5cb9-a2b8-bfdc4ceb73b4",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.trainer.IronDefender.Name",
    display_name="Iron Defender",
    searchable_by=["Iron Defender","Item","IronDefender"],
    subtypes=["Item"],
    collector_number=118,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    effect=iron_defender,
)
