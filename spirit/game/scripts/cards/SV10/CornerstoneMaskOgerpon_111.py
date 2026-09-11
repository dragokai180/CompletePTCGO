from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4cd26fdb-7421-554e-869f-2342e5cc99e1",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.CornerstoneMaskOgerpon.Name",
    display_name="Cornerstone Mask Ogerpon",
    searchable_by=["Cornerstone Mask Ogerpon", "Basic", "CornerstoneMaskOgerpon"],
    subtypes=["Basic"],
    collector_number=111,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=1017,
    abilities=[
        Attack(
            title="Rock Kagura",
            game_text="Search your deck for a Basic Fighting Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Mountain Ramming",
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
