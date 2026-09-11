from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="2e5d208b-d544-51df-9508-5c784a705da5",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LandorusEX.Name",
    display_name="Landorus-EX",
    searchable_by=["Landorus-EX","Basic","EX","LandorusEX"],
    subtypes=["Basic","EX"],
    collector_number=89,
    set_code="BW7",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    abilities=[
        Attack(
            title="Hammerhead",
            game_text="Does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Land's Judgment",
            game_text="You may discard all Fighting Energy attached to this Pokémon. If you do, this attack does 70 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
