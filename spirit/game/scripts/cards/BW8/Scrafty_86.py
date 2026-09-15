from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.bw10 import aura_of_the_land, knock_back, shadow_punch, sinister_hand, sinister_hand_condition
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

card = PokemonCardDef(
    guid="fcfca166-cf6b-5321-8416-d4a9ee7d0879",
    key="BW8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scrafty.Name",
    display_name="Scrafty",
    searchable_by=["Scrafty","Stage 1","Scrafty","Team Plasma"],
    subtypes=["Stage 1","Team Plasma"],
    collector_number=86,
    set_code="BW8",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scraggy.Name",
    abilities=[
        Attack(
            title="Kick Away",
            game_text="Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=knock_back,
        ),
        Attack(
            title="Reinforced Headbutt",
            game_text="If this Pokémon has a Pokémon Tool card attached to it, this attack does 50 more damage.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator="+",
            effect=bw_legacy_attack,
        ),
    ],
)
