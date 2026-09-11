from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="a6672b87-cd52-56f0-83de-30bb1084c53c",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon","Stage 2","Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=103,
    set_code="BW4",
    rarity=Rarities.RareSecret,
    hp=150,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    abilities=[
        Ability(
            title="Dark Aura",
            game_text="All Energy attached to this Pokémon are Darkness Energy instead of their usual type.",
            passive=bw_legacy_passive("All Energy attached to this Pokémon are Darkness Energy instead of their usual type."),
        ),
        Attack(
            title="Berserker Blade",
            game_text="Does 40 damage to 2 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 4},
            damage=60,
            effect=bw_legacy_attack,
        ),
    ],
)
