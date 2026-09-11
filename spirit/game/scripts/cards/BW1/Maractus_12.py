from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="3594d136-d42c-58ab-b9a3-e9f4900000a2",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Maractus.Name",
    display_name="Maractus",
    searchable_by=["Maractus","Basic","Maractus"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Constant Rattle",
            game_text="Flip 3 coins. If 1 of them is heads, this attack does 10 damage. If 2 of them are heads, this attack does 30 damage. If all of them are heads, this attack does 60 damage.",
            cost={PokemonTypes.GRASS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Giga Drain",
            game_text="Heal from this Pokémon the same amount of damage you did to the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 3},
            damage=50,
            effect=leech_life,
        ),
    ],
)
