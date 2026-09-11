from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="fa895c57-e1b1-580b-b5ce-ae920fd18829",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    display_name="Brionne",
    searchable_by=["Brionne", "Stage 1", "Brionne"],
    subtypes=["Stage 1"],
    collector_number=19,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name",
    family_id=728,
    abilities=[
        Attack(
            title="Hyper Voice",
            cost={PokemonTypes.WATER: 1},
            damage=40,
        ),
    ],
)
