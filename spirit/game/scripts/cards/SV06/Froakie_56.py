from spirit.game.data_utils import PokemonCardDef, Attack, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import search_to_bench


def _is_froakie(card) -> bool:
    definition = def_for(card.archetype_id)
    return definition is not None and definition.display_name == "Froakie"


card = PokemonCardDef(
    guid="b9b1e08c-986d-48c1-a8a7-6c0914a0ab90",
    key="SV06",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name",
    display_name="Froakie",
    searchable_by=["Froakie", "Basic", "Froakie"],
    subtypes=["Basic"],
    collector_number=56,
    set_code="SV06",
    regulation_mark="H",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=656,
    abilities=[
        Attack(
            title="Flock",
            game_text=(
                "Search your deck for up to 2 Froakie and put them onto your Bench. "
                "Then, shuffle your deck."
            ),
            cost={PokemonTypes.WATER: 1},
            effect=search_to_bench(predicate=_is_froakie, count=2),
        ),
        Attack(
            title="Flop",
            game_text="",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)

