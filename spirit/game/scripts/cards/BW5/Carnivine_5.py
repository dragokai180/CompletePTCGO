from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="452c164c-1029-5c52-a72a-acf8401510dc",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name",
    display_name="Carnivine",
    searchable_by=["Carnivine","Basic","Carnivine"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    abilities=[
        Attack(
            title="Lure Poison",
            game_text="Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon. The new Defending Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Spit Squall",
            game_text="Your opponent puts the Defending Pokémon and all cards attached to it into his or her hand.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
    ],
)
