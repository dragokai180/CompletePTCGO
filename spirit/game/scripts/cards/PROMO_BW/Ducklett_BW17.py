from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="4a655a80-678d-5455-b997-c6413298aacb",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ducklett.Name",
    display_name="Ducklett",
    searchable_by=["Ducklett","Basic","Ducklett"],
    subtypes=["Basic"],
    collector_number=17,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
