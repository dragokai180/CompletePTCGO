from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="edd8ae00-5fdc-5a2b-bb6f-d4c90c0aa99b",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsDarumaka.Name",
    display_name="N's Darumaka",
    searchable_by=["N's Darumaka", "Basic", "NsDarumaka"],
    subtypes=["Basic"],
    collector_number=26,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    family_id=554,
    abilities=[
        Attack(
            title="Rolling Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Flare",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
