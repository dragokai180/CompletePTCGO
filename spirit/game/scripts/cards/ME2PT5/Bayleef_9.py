from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="d1cb3a9e-cd46-5ea8-b344-080aa220ab31",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    display_name="Bayleef",
    searchable_by=["Bayleef","Stage 1","Bayleef"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="ME2PT5",
    regulation_mark="J",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    family_id=152,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Chikorita.Name",
    abilities=[
        Attack(
            title="Leaf Step",
            cost={PokemonTypes.GRASS: 2},
            damage=60,
        ),
    ],
)
