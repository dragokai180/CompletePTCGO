from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="8dbc2a03-62b3-58be-9871-b87694c4e1a9",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Throh.Name",
    display_name="Throh",
    searchable_by=["Throh","Basic","Throh"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="BW6",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Attack(
            title="Squeeze",
            game_text="Flip a coin. If heads, this attack does 20 more damage and the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Superpower",
            game_text="You may do 20 more damage. If you do, this Pokémon does 20 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
