from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers, movable_energy_condition

card = PokemonCardDef(
    guid="20f4457b-d63c-59f4-987e-b9ce2946ae72",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon","Stage 2","Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=97,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    abilities=[
        Ability(
            title="Dark Trance",
            game_text="As often as you like during your turn (before your attack), you may move a Darkness Energy attached to 1 of your Pokémon to another of your Pokémon.",
            activation="unlimited",
            effect=bw_legacy_ability,
            condition=movable_energy_condition(PokemonTypes.DARKNESS),
        ),
        Attack(
            title="Dragonblast",
            game_text="Discard 2 Darkness Energy attached to this Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=bw_legacy_attack,
        ),
    ],
)
