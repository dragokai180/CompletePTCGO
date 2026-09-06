from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.passives_common import protect_next_turn


def chaos_crawler_condition(board, player_id, pokemon):
    """Unusable if any of your Pokémon used Chaos Crawler last turn."""
    prev = board.turn_state.attack_titles_prev_turn_by_player.get(player_id) or []
    return "Chaos Crawler" not in prev


card = PokemonCardDef(
    guid="a3e42cf2-fd82-5899-884a-cd3548f1d510",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name",
    display_name="Giratina",
    searchable_by=["Giratina","Basic","Giratina"],
    subtypes=["Basic"],
    collector_number=31,
    set_code="ME6",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    family_id=487,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    abilities=[
        Attack(
            title="Chaos Crawler",
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks. This attack can't be used if any of your Pokémon used Chaos Crawler during your last turn.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            condition=chaos_crawler_condition,
            effect=protect_next_turn(prevent=True),
        ),
    ],
)
