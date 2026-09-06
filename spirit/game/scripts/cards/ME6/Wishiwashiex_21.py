from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import in_active_spot
from spirit.game.session.passives import effective_max_hp


def _ocean_gain_ok(board, player_id, pokemon):
    if not in_active_spot(board, player_id, pokemon):
        return False
    return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(board, pokemon)


async def ocean_gain(ctx):
    """Heal 50 damage from this Pokémon."""
    await ctx.heal(50, ctx.source)


card = PokemonCardDef(
    guid="fcdf3257-567f-54c0-ab5f-08ba9720642e",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashiex.Name",
    display_name="Wishiwashi ex",
    searchable_by=["Wishiwashi ex","Basic","ex","Wishiwashiex"],
    subtypes=["Basic","ex"],
    collector_number=21,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=260,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=746,
    abilities=[
        Ability(
            title="Ocean Gain",
            game_text="You may use this Ability once during your turn, if this Pokémon is in the Active Spot. Heal 50 damage from this Pokémon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_ocean_gain_ok,
            effect=ocean_gain,
        ),
        Attack(
            title="Hydro Splash",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=220,
        ),
    ],
)
