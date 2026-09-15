from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="ed37d0b0-5200-5531-8141-b235ee150c17",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Virizion.Name",
    display_name="Virizion",
    searchable_by=["Virizion","Basic","Virizion"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Giga Drain",
            game_text="Heal from this Pokémon the same amount of damage you did to the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=leech_life,
        ),
        Attack(
            title="Sacred Sword",
            game_text="This Pokémon can't use Sacred Sword during your next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=bw_legacy_attack,
        ),
    ],
)
