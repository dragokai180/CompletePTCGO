from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="49784359-0db9-57bd-91d6-d19d79d7cd60",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bulbasaur.Name",
    display_name="Bulbasaur",
    searchable_by=["Bulbasaur","Basic","Bulbasaur"],
    subtypes=["Basic"],
    collector_number=1,
    set_code="ME1",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    family_id=1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    abilities=[
        Attack(
            title="Bind Down",
            game_text="During your opponent's next turn, the Defending Pokémon can't retreat.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=condition_attack(no_retreat=True),
        ),
    ],
)
