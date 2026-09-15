from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack, flip_damage
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="60228673-c295-5041-b0d7-0f2e1ed8977b",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss","Stage 1","Amoonguss"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="BW3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    abilities=[
        Attack(
            title="Toxic",
            game_text="The Defending Pokémon is now Poisoned. Put 2 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.GRASS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)
