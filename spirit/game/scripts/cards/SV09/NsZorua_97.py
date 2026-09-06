from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="b13f5cd3-78a2-52f9-bb5b-2766e32942db",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsZorua.Name",
    display_name="N's Zorua",
    searchable_by=["N's Zorua", "Basic", "NsZorua"],
    subtypes=["Basic"],
    collector_number=97,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=570,
    abilities=[
        Attack(
            title="Scratch",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
        ),
    ],
)
