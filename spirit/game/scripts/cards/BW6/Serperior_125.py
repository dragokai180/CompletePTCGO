from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="29f0368e-9b76-5191-9be8-eb676410bcf6",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperior.Name",
    display_name="Serperior",
    searchable_by=["Serperior","Stage 2","Serperior"],
    subtypes=["Stage 2"],
    collector_number=125,
    set_code="BW6",
    rarity=Rarities.RareSecret,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    abilities=[
        Ability(
            title="Royal Heal",
            game_text="At any times between turns, heal 10 damage from each of your Pokémon.",
            trigger="between_turns",
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Leaf Tornado",
            game_text="Move as many Grass Energy attached to your Pokémon to your other Pokémon in any way you like.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=bw_legacy_attack,
        ),
    ],
)
