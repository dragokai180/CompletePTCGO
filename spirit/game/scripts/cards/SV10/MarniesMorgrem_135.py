from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="26743eba-d14e-5407-ba80-a7975a74d55f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesMorgrem.Name",
    display_name="Marnie's Morgrem",
    searchable_by=["Marnie's Morgrem", "Stage 1", "MarniesMorgrem"],
    subtypes=["Stage 1"],
    collector_number=135,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesImpidimp.Name",
    family_id=859,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.DARKNESS: 2},
            damage=60,
        ),
    ],
)
