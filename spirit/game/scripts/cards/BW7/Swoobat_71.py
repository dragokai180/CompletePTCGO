from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import acrobatics, swift_dive
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="08b45b0a-f763-570f-b3cf-dbea70b6abe3",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name",
    display_name="Swoobat",
    searchable_by=["Swoobat","Stage 1","Swoobat"],
    subtypes=["Stage 1"],
    collector_number=71,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name",
    abilities=[
        Attack(
            title="Jet Woofer",
            game_text="For each Psychic Energy attached to this Pokémon, discard the top card of your opponent's deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=bw_legacy_attack,
        ),
        Attack(
            title="Acrobatics",
            game_text="Flip 2 coins. This attack does 20 more damage for each heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="+",
            effect=acrobatics,
        ),
    ],
)
