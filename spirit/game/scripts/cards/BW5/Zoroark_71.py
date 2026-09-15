from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="cf4fe2e9-e1bf-5880-bcfb-bb2336527157",
    key="BW5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name",
    display_name="Zoroark",
    searchable_by=["Zoroark","Stage 1","Zoroark"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="BW5",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name",
    abilities=[
        Attack(
            title="Brutal Bash",
            game_text="Does 20 damage times the number of Darkness Pokémon you have in play.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Dark Rush",
            game_text="Does 20 damage times the number of damage counters on this Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=20,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
    ],
)
