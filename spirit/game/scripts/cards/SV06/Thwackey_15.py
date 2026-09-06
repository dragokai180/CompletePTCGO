from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import pokemon_has_ability_titled
from spirit.game.session.passives import ability_locked


def _boom_boom_groove_condition(board, player_id, pokemon) -> bool:
    active = board.active_pokemon(player_id)
    if active is None or ability_locked(board, active):
        return False
    if not pokemon_has_ability_titled(active, "Festival Lead"):
        return False
    deck = board.find_player_area(player_id, "deck")
    return bool(deck and deck.children)


async def boom_boom_groove(ctx):
    """Search your deck for a card and put it into your hand. Shuffle."""
    picks = await ctx.search_deck(
        count=1, minimum=0,
        prompt="Choose a card to put into your hand.",
    )
    await ctx.put_in_hand(picks, reveal=False)
    await ctx.shuffle_deck()


card = PokemonCardDef(
    guid="971dad66-c354-5eff-b210-b4f9127525ca",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thwackey.Name",
    display_name="Thwackey",
    searchable_by=["Thwackey", "Stage 1", "Thwackey"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Grookey.Name",
    family_id=810,
    abilities=[
        Ability(
            title="Boom Boom Groove",
            game_text="Once during your turn, if your Active Pokémon has the Festival Lead Ability, you may search your deck for a card and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            condition=_boom_boom_groove_condition,
            effect=boom_boom_groove,
        ),
        Attack(
            title="Beat",
            cost={PokemonTypes.GRASS: 2},
            damage=50,
        ),
    ],
)
