from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.session.effects import is_pokemon_card


def _is_colorless_pokemon_100_or_less(card) -> bool:
    if not is_pokemon_card(card):
        return False
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    if PokemonTypes.COLORLESS.value not in types:
        return False
    return (card.get_attribute(AttrID.HP, 999) or 0) <= 100


def _is_players_first_turn(board, player_id, pokemon=None) -> bool:
    """True on this player's first turn (turn 1 going first, turn 2 going second)."""
    ts = getattr(board, "turn_state", None)
    return ts is not None and ts.turn_number <= 2


async def fan_call(ctx):
    """Search for up to 3 Colorless Pokémon with 100 HP or less."""
    picks = await ctx.search_deck(
        _is_colorless_pokemon_100_or_less, count=3, minimum=0,
        prompt="Choose up to 3 Colorless Pokémon with 100 HP or less.",
    )
    await ctx.put_in_hand(picks, reveal=True)
    await ctx.shuffle_deck()


async def assault_landing(ctx):
    """70. If there is no Stadium in play, this attack does nothing."""
    if ctx.stadium_in_play() is None:
        return
    await ctx.deal_damage()


card = PokemonCardDef(
    guid="b89fa770-19df-5c4a-95e9-7564fe8257ae",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FanRotom.Name",
    display_name="Fan Rotom",
    searchable_by=["Fan Rotom", "Basic", "FanRotom"],
    subtypes=["Basic"],
    collector_number=118,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=479,
    abilities=[
        Ability(
            title="Fan Call",
            game_text=(
                "Once during your first turn, you may search your deck for up "
                "to 3 [C] Pokémon with 100 HP or less, reveal them, and put "
                "them into your hand. Then, shuffle your deck. You can't use "
                "more than 1 Fan Call Ability during your turn."
            ),
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Fan Call",
            condition=_is_players_first_turn,
            effect=fan_call,
        ),
        Attack(
            title="Assault Landing",
            game_text="If there is no Stadium in play, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=assault_landing,
        ),
    ],
)
