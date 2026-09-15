from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="2b40d02f-9532-5cc1-8f56-43c8e4754ec4",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RegisteelEX.Name",
    display_name="Registeel-EX",
    searchable_by=["Registeel-EX","Basic","EX","RegisteelEX"],
    subtypes=["Basic","EX"],
    collector_number=122,
    set_code="BW6",
    rarity=Rarities.RareUltra,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Triple Laser",
            game_text="This attack does 30 damage to 3 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon).",
            cost={PokemonTypes.COLORLESS: 3},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Protect Charge",
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=bw_legacy_attack,
        ),
    ],
)
