from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="efa56932-8ec7-58a2-952d-27671eaa4865",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name",
    display_name="Cubchoo",
    searchable_by=["Cubchoo","Basic","Cubchoo"],
    subtypes=["Basic"],
    collector_number=29,
    set_code="BW2",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    abilities=[
        Attack(
            title="Icicle Punch",
            cost={PokemonTypes.WATER: 2},
            damage=30,
        ),
    ],
)
