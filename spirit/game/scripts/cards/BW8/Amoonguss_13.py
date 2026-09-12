from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="655d3016-30d4-5c53-9fef-eead32738dbf",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Amoonguss.Name",
    display_name="Amoonguss",
    searchable_by=["Amoonguss","Stage 1","Amoonguss","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=13,
    set_code="BW8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name",
    abilities=[
        Attack(
            title="Astonish",
            game_text="Flip a coin. If heads, choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into his or her deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Miracle Powder",
            game_text="Flip a coin. If heads, choose a Special Condition. The Defending Pokémon is now affected by that Special Condition.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=bw_legacy_attack,
        ),
    ],
)
