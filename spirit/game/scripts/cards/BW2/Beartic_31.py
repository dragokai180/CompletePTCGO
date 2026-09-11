from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import deluge, deluge_condition, hydro_pump, powder_snow, reflect_energy
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="f3a0b133-704b-5142-a78e-72b712c7beb2",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beartic.Name",
    display_name="Beartic",
    searchable_by=["Beartic","Stage 1","Beartic"],
    subtypes=["Stage 1"],
    collector_number=31,
    set_code="BW2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    abilities=[
        Attack(
            title="Icy Wind",
            game_text="The Defending Pokémon is now Asleep.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=powder_snow,
        ),
        Attack(
            title="Superpower",
            game_text="You may do 20 more damage. If you do, this Pokémon does 20 damage to itself.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
