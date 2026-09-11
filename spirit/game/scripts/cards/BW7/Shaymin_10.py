from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import call_for_family, comet_punch
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="79386055-e551-5742-b1ef-ff18a1b0dd66",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shaymin.Name",
    display_name="Shaymin",
    searchable_by=["Shaymin","Basic","Shaymin"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Call for Family",
            game_text="Search your deck for 2 Basic Pokémon and put them onto your Bench. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=call_for_family,
        ),
        Attack(
            title="Leaf Drain",
            game_text="Flip a coin. If heads, heal 30 damage from this Pokémon.",
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=bw_legacy_attack,
        ),
    ],
)
