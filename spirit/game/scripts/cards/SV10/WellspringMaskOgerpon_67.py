from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="03f0e02f-f9d3-561a-9896-c9e1df2083bb",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.WellspringMaskOgerpon.Name",
    display_name="Wellspring Mask Ogerpon",
    searchable_by=["Wellspring Mask Ogerpon", "Basic", "WellspringMaskOgerpon"],
    subtypes=["Basic"],
    collector_number=67,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=1017,
    abilities=[
        Attack(
            title="Water Kagura",
            game_text="Search your deck for a Basic Water Energy card and attach it to 1 of your Pokémon. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Bubble Drain",
            game_text="Heal 30 damage from this Pokémon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
