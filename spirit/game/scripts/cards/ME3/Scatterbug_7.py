from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="bfc216ad-cdaf-5ab6-b77f-d28eb732e689",
    key="ME3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name",
    display_name="Scatterbug",
    searchable_by=["Scatterbug", "Basic", "Scatterbug"],
    subtypes=["Basic"],
    collector_number=7,
    set_code="ME3",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=664,
    abilities=[
        Attack(
            title="Gnaw",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
