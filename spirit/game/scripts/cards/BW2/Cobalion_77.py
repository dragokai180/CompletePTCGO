from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import aura_of_the_land, knock_back, shadow_punch, sinister_hand, sinister_hand_condition
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="687f256a-ab29-5b33-8c60-4c3ab9125956",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cobalion.Name",
    display_name="Cobalion",
    searchable_by=["Cobalion","Basic","Cobalion"],
    subtypes=["Basic"],
    collector_number=77,
    set_code="BW2",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Metal Horns",
            game_text="Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=knock_back,
        ),
        Attack(
            title="Sacred Sword",
            game_text="This Pokémon can't use Sacred Sword during your next turn.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=bw_legacy_attack,
        ),
    ],
)
