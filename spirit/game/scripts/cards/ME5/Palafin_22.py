from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="edd7ee4e-7c35-59b5-af75-82db66830f7b",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Palafin.Name",
    display_name="Palafin",
    searchable_by=["Palafin", "Stage 1", "Palafin"],
    subtypes=["Stage 1"],
    collector_number=22,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name",
    family_id=963,
    abilities=[
        Attack(
            title="Knuckle Justice",
            game_text="If your opponent has exactly 1 Prize card remaining, this attack does 200 more damage.",
            cost={PokemonTypes.WATER: 2},
            damage=80,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
