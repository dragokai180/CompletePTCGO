from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="c57532ce-c4aa-5530-b946-caae63f99031",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    display_name="Riolu",
    searchable_by=["Riolu","Basic","Riolu"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=447,
    abilities=[
        Attack(
            title="Accelerating Stab",
            game_text="During your next turn, this Pokémon can't use Accelerating Stab.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            locks_next_turn=True,
        ),
    ],
)
