from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="0c5d265d-7eb2-5a0c-8ea7-9c1a916f762b",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mandibuzz.Name",
    display_name="Mandibuzz",
    searchable_by=["Mandibuzz","Stage 1","Mandibuzz"],
    subtypes=["Stage 1"],
    collector_number=73,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vullaby.Name",
    abilities=[
        Attack(
            title="Blindside",
            game_text="Does 50 damage to 1 of your opponent's Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Punishment",
            game_text="If the Defending Pokémon is a Stage 2 Pokémon, this attack does 60 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
