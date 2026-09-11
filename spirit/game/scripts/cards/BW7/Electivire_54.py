from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import damage_all_opponents
from spirit.game.card_effects.bw10 import giga_frost, outrage, shadow_punch, sinister_hand, sinister_hand_condition

card = PokemonCardDef(
    guid="40f27a35-fe70-5b44-b2d9-944ff93b240b",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name",
    display_name="Electivire",
    searchable_by=["Electivire","Stage 1","Electivire"],
    subtypes=["Stage 1"],
    collector_number=54,
    set_code="BW7",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name",
    abilities=[
        Attack(
            title="Electriwave",
            game_text="This attack does 30 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            effect=damage_all_opponents(30),
        ),
        Attack(
            title="Shock Wave",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=shadow_punch,
        ),
    ],
)
