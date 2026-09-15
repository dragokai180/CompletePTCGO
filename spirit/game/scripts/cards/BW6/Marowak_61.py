from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import blazing_claws, dark_clamp, leech_life, solar_transporter
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="e437c845-53fa-575d-adda-d84063f4fc48",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name",
    display_name="Marowak",
    searchable_by=["Marowak","Stage 1","Marowak"],
    subtypes=["Stage 1"],
    collector_number=61,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    abilities=[
        Attack(
            title="Bone Lock",
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=dark_clamp,
        ),
        Attack(
            title="Vortex Chop",
            game_text="If the Defending Pokémon has any Resistance, this attack does 30 more damage.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
