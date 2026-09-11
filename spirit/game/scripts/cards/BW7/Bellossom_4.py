from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="90482447-b846-562a-bda3-621110d1fe22",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name",
    display_name="Bellossom",
    searchable_by=["Bellossom","Stage 2","Bellossom"],
    subtypes=["Stage 2"],
    collector_number=4,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name",
    abilities=[
        Attack(
            title="Grass Knot",
            game_text="Does 20 more damage for each Colorless in the Defending Pokémon's Retreat Cost.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Petal Dance",
            game_text="Flip 3 coins. This attack does 50 damage times the number of heads. This Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator="x",
            effect=bw_legacy_attack,
        ),
    ],
)
