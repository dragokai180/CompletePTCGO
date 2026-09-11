from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="29778367-60e7-549a-83b9-f14d243b63b4",
    key="SV07",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.RagingBolt.Name",
    display_name="Raging Bolt",
    searchable_by=["Raging Bolt", "Basic", "Ancient", "RagingBolt"],
    subtypes=["Basic", "Ancient"],
    collector_number=111,
    set_code="SV07",
    regulation_mark="H",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=1021,
    abilities=[
        Attack(
            title="Thunderburst Storm",
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon for each Energy attached to this Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Dragon Headbutt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
