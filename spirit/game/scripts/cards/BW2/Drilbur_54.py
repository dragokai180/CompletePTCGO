from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="627abe51-2952-5290-8474-cb995a2092fc",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur","Basic","Drilbur"],
    subtypes=["Basic"],
    collector_number=54,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Hone Claws",
            game_text="During your next turn, each of this Pokémon's attacks does 30 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Scratch",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
