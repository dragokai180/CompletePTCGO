from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import creepy_wind, wind_blast
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="e0de1565-2a82-55ef-8e58-e1bcd0419945",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name",
    display_name="Skarmory",
    searchable_by=["Skarmory","Basic","Skarmory"],
    subtypes=["Basic"],
    collector_number=96,
    set_code="BW7",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Metal Sound",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Confused.",
            cost={PokemonTypes.METAL: 1},
            effect=creepy_wind,
        ),
        Attack(
            title="Swift",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on the Defending Pokémon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=bw_legacy_attack,
        ),
    ],
)
