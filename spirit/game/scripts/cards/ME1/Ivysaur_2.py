from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="a05845e0-1d37-5f46-8069-ae8b6aa322cf",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ivysaur.Name",
    display_name="Ivysaur",
    searchable_by=["Ivysaur","Stage 1","Ivysaur"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    family_id=1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    abilities=[
        Attack(
            title="Razor Leaf",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
        ),
    ],
)
