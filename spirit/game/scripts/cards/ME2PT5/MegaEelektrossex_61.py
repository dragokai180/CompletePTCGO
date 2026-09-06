from spirit.game.data_utils import PokemonCardDef, Attack, unimplemented
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="70ddf21e-0504-59e6-b683-06b5db02f673",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaEelektrossex.Name",
    display_name="Mega Eelektross ex",
    searchable_by=["Mega Eelektross ex","Stage 1","Stage 2","ex","SV_Mega","MegaEelektrossex"],
    subtypes=["Stage 1","Stage 2","ex","SV_Mega"],
    collector_number=61,
    set_code="ME2PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=350,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Split Bomb",
            game_text="This attack does 60 damage to each of 2 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 2},
            effect=unimplemented,
        ),
        Attack(
            title="Disaster Shock",
            game_text="You may discard 2 Lightning Energy from this Pokémon and make your opponent's Active Pokémon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=190,
            effect=unimplemented,
        ),
    ],
)
