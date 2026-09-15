from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="08e542e8-4979-5072-8f8a-c13f5d071699",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Petilil.Name",
    display_name="Petilil",
    searchable_by=["Petilil","Basic","Petilil"],
    subtypes=["Basic"],
    collector_number=9,
    set_code="BW1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Magical Leaf",
            game_text="Flip a coin. If heads, this attack does 10 more damage and heal 10 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
