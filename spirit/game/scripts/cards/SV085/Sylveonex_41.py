from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import debuff_defender_attacks
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.session.effects import full_stack


def _angelite_condition(board, player_id, pokemon):
    opponent = next((pid for pid in board.player_ids if pid != player_id), None)
    if opponent is None:
        return False
    bench = board.find_player_area(opponent, "bench")
    if bench is None or len(bench.children) < 2:
        return False
    ts = getattr(board, "turn_state", None)
    if ts is None:
        return True
    for used_id, _archetype, title in ts.attacks_used_last_turn:
        if title != "Angelite":
            continue
        entity = board.get_entity(used_id)
        if entity is not None and entity.owning_player_id == player_id:
            return False
    return True


async def angelite(ctx):
    """Choose 2 of your opponent's Benched Pokémon. Shuffle those Pokémon
    and all attached cards into your opponent's deck."""
    bench = [p for p in ctx.opponent_bench() if not ctx.effects_blocked(p)]
    if len(bench) < 2:
        return
    picks = await ctx.choose_cards(
        bench, 2, minimum=2,
        prompt="Choose 2 of your opponent's Benched Pokémon",
    )
    cards = [card for pokemon in picks for card in full_stack(pokemon)]
    if cards:
        await ctx.shuffle_into_deck(cards, ctx.opponent_id)


card = PokemonCardDef(
    guid="c3da966c-5542-533e-b982-873692bbb3cb",
    key="SV085",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sylveonex.Name",
    display_name="Sylveon ex",
    searchable_by=["Sylveon ex","Stage 1","ex","Tera","Sylveonex"],
    subtypes=["Stage 1","ex","Tera"],
    collector_number=41,
    set_code="SV085",
    regulation_mark="H",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    family_id=133,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    passive=TeraRulePassive(),
    abilities=[
        Attack(
            title="Magical Charm",
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 100 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=160,
            effect=debuff_defender_attacks(100),
        ),
        Attack(
            title="Angelite",
            game_text="Choose 2 of your opponent's Benched Pokémon. Shuffle those Pokémon and all attached cards into your opponent's deck. If 1 of your Pokémon used Angelite during your last turn, this attack can't be used.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1, PokemonTypes.PSYCHIC: 1},
            condition=_angelite_condition,
            effect=angelite,
        ),
    ],
)
