from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_basic_fighting_energy(card):
    types = card.get_attribute(AttrID.POKEMON_TYPES) or []
    return is_basic_energy_card(card) and PokemonTypes.FIGHTING.value in types


def lunar_cycle_condition(board, player_id, pokemon):
    if not any(p.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == "Solrock"
               for p in board.pokemon_in_play(player_id)):
        return False
    hand = board.find_player_area(player_id, "hand")
    return bool(hand) and any(_is_basic_fighting_energy(c) for c in hand.children)


async def lunar_cycle(ctx):
    """Once during your turn, if you have Solrock in play, you may discard a
    Basic Fighting Energy card from your hand in order to use this Ability.
    Draw 3 cards. You can't use more than 1 Lunar Cycle Ability each turn."""
    discarded = await ctx.discard_from_hand(
        1, predicate=_is_basic_fighting_energy,
        prompt="Discard a Basic Fighting Energy card",
    )
    if discarded:
        await ctx.draw_cards(3)


card = PokemonCardDef(
    guid="b07c40c6-f621-54ca-b3aa-52bb7402ec7c",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone","Basic","Lunatone"],
    subtypes=["Basic"],
    collector_number=74,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=337,
    abilities=[
        Ability(
            title="Lunar Cycle",
            game_text="Once during your turn, if you have Solrock in play, you may discard a Basic Fighting Energy card from your hand in order to use this Ability. Draw 3 cards. You can't use more than 1 Lunar Cycle Ability each turn.",
            activation=Activations.ONCE_PER_TURN,
            shared_once_per_turn="Lunar Cycle",
            condition=lunar_cycle_condition,
            effect=lunar_cycle,
        ),
        Attack(
            title="Power Gem",
            cost={PokemonTypes.FIGHTING: 2},
            damage=50,
        ),
    ],
)
