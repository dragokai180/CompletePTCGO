from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="a86f8f44-daa3-5ca2-8552-aa226398f478",
    key="BW1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Liepard.Name",
    display_name="Liepard",
    searchable_by=["Liepard","Stage 1","Liepard"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="BW1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Purrloin.Name",
    abilities=[
        Attack(
            title="Taunt",
            game_text="Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Sucker Punch",
            game_text="If this Pokémon has any Darkness Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
