from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack


from spirit.game.card_effects.attacks_common import previous_attack_matches


def _togedemaru_toge_dash_condition(board, player_id, pokemon):
    return previous_attack_matches(board, player_id, name="Togedemaru", title="Toge Dash")

card = PokemonCardDef(
    guid="39aa098f-3cab-5aeb-a8e0-99750798b010",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dedenne.Name",
    display_name="Dedenne",
    searchable_by=["Dedenne", "Basic", "Dedenne"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="SWSH12",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=702,
    abilities=[
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Dede-Short",
            game_text="You can use this attack only if 1 of your Togedemaru used Toge Dash during your last turn. Your opponent's Active Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=60,
            condition=_togedemaru_toge_dash_condition,
            effect=condition_attack(SpecialConditions.PARALYZED),
        ),
    ],
)
