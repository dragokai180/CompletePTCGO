from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import debuff_defender_attacks
from spirit.game.card_effects.pokemon import TeraRulePassive
from spirit.game.session.effects import full_stack
from spirit.game.card_effects.attack_requirements import printed_attack_allowed


def _angelite_condition(board, player_id, pokemon):
    return printed_attack_allowed(
        "If 1 of your Pokémon used Angelite during your last turn, this attack can't be used.",
        board, player_id, pokemon)


async def angelite(ctx):
    """Choose 2 of your opponent's Benched Pokémon. Shuffle those Pokémon
    and all attached cards into your opponent's deck."""
    if not _angelite_condition(ctx.board, ctx.player_id, ctx.attacker):
        return
    bench = list(ctx.opponent_bench())
    if not bench:
        return
    count = min(2, len(bench))
    picks = await ctx.choose_cards(
        bench, count, minimum=count,
        prompt="Choose your opponent's Benched Pokémon",
    )
    cards = [card for pokemon in picks if not ctx.effects_blocked(pokemon)
             for card in full_stack(pokemon)]
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
