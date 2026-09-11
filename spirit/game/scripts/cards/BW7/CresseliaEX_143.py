from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw_era import bw_legacy_ability, bw_legacy_attack, bw_legacy_passive, bw_stadium_ability, bw_stadium_triggers, bw_tool_abilities, bw_trainer_effect, bw_trainer_passive

card = PokemonCardDef(
    guid="2d14885c-a6db-55b6-8a63-0742c340ca2d",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CresseliaEX.Name",
    display_name="Cresselia-EX",
    searchable_by=["Cresselia-EX","Basic","EX","CresseliaEX"],
    subtypes=["Basic","EX"],
    collector_number=143,
    set_code="BW7",
    rarity=Rarities.RareUltra,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    abilities=[
        Ability(
            title="Sparkling Particles",
            game_text="At any time between turns, heal 10 damage from this Pokémon.",
            trigger="between_turns",
            effect=bw_legacy_ability,
        ),
        Attack(
            title="Psychic Protection",
            game_text="During your opponent's next turn, this Pokémon has no Weakness.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            effect=bw_legacy_attack,
        ),
    ],
)
