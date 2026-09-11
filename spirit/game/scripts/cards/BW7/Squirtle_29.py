from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, flip_or_nothing
from spirit.game.card_effects.passives_common import prevent_damage_when

def _shell_shield_pred(calc, carrier):
    return calc.is_attack and calc.target is carrier and not calc.to_active

card = PokemonCardDef(
    guid="6d9a9ccf-b043-56d2-86d3-8dff78e6c9cb",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle","Basic","Squirtle"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="BW7",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    abilities=[
        Ability(
            title="Shell Shield",
            game_text="As along as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=prevent_damage_when(_shell_shield_pred, attacks_only=False),
        ),
        Attack(
            title="Water Splash",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
