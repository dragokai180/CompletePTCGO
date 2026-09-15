from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="20fda90b-8a8f-57bf-a782-0ef4394f9a82",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name",
    display_name="Golett",
    searchable_by=["Golett","Basic","Golett"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="BW3",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Dynamic Punch",
            game_text="Flip a coin. If heads, this attack does 20 more damage and the Defending Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=bw_legacy_attack,
        ),
    ],
)
