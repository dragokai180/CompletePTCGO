from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="058e9e24-e235-5429-84a9-c1a93cac5bd5",
    key="PROMO_BW",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pidove.Name",
    display_name="Pidove",
    searchable_by=["Pidove","Basic","Pidove"],
    subtypes=["Basic"],
    collector_number=15,
    set_code="PROMO_BW",
    rarity=Rarities.RarePromo,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    abilities=[
        Attack(
            title="Gust",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
