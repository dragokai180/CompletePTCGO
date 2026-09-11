from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="0e7caebe-07a0-500f-af33-1f52a7070f7d",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic", "Zarude"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=893,
    abilities=[
        Attack(
            title="Overhead Throw",
            game_text="This attack also does 30 damage to 1 of your Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.DARKNESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title="Shadowy Whip",
            game_text="If your Benched Pokémon have any Shadowy Darkness Energy attached, this attack does 70 more damage.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=100,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
