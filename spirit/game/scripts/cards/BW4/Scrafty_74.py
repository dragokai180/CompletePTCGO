from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="4ac62b0e-de77-5585-9fbb-284e2462169d",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty","Stage 1","Scrafty"],
    subtypes=["Stage 1"],
    collector_number=74,
    set_code="BW4",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    abilities=[
        Attack(
            title="Rock Head",
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Hammer Kick",
            game_text="If this Pokémon has fewer remaining HP than the Defending Pokémon, this attack does 30 more damage.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
