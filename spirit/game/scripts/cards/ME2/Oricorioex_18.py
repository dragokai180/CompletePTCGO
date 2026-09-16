from spirit.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, is_pokemon_ex, subtypes_for,
)
from spirit.game.attributes import AttrID, PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.card_effects.trainers import is_basic_energy_card


def _is_fire(pokemon):
    types = pokemon.get_attribute(AttrID.POKEMON_TYPES) or []
    return PokemonTypes.FIRE.value in types


def _is_basic_fire_energy(card):
    return is_basic_energy_card(card) and energy_provides_type(
        card, PokemonTypes.FIRE.value)


def _has_fire_mega_ex(board, player_id):
    for pokemon in board.pokemon_in_play(player_id):
        if (
            _is_fire(pokemon)
            and "SV_Mega" in subtypes_for(pokemon.archetype_id)
            and is_pokemon_ex(pokemon.archetype_id)
        ):
            return True
    return False


def excited_turbo_condition(board, player_id, pokemon):
    if not _has_fire_mega_ex(board, player_id):
        return False
    hand = board.find_player_area(player_id, "hand")
    if not hand or not any(_is_basic_fire_energy(c) for c in hand.children):
        return False
    bench = board.find_player_area(player_id, "bench")
    return bool(bench) and any(_is_fire(p) for p in bench.children)


async def excited_turbo(ctx):
    """Attach a Basic Fire Energy from hand to 1 of your Benched Fire Pokémon."""
    await ctx.attach_from_hand_freely(
        _is_basic_fire_energy,
        lambda: [p for p in ctx.my_bench() if _is_fire(p)]
        if _has_fire_mega_ex(ctx.board, ctx.player_id) else [],
        "Choose a Basic Fire Energy to attach, or Done")


card = PokemonCardDef(
    guid="75cf17c3-1619-5a18-8fc1-2423a28c634b",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Oricorioex.Name",
    display_name="Oricorio ex",
    searchable_by=["Oricorio ex","Basic","ex","Oricorioex"],
    subtypes=["Basic","ex"],
    collector_number=18,
    set_code="ME2",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    family_id=741,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    abilities=[
        Ability(
            title="Excited Turbo",
            game_text="As often as you like during your turn, if you have any Fire Mega Evolution Pokémon ex in play, you may use this Ability. Attach a Basic Fire Energy card from your hand to 1 of your Benched Fire Pokémon.",
            activation=Activations.UNLIMITED,
            condition=excited_turbo_condition,
            effect=excited_turbo,
        ),
        Attack(
            title="Fire Wing",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
    ],
)
