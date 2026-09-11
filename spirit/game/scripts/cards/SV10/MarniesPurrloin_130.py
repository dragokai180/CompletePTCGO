from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="d4de86b0-356c-5a50-970c-a74e0291ad9f",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MarniesPurrloin.Name",
    display_name="Marnie's Purrloin",
    searchable_by=["Marnie's Purrloin", "Basic", "MarniesPurrloin"],
    subtypes=["Basic"],
    collector_number=130,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=509,
    abilities=[
        Attack(
            title="Pointy Nails",
            game_text="If your opponent's Active Pokémon is a Pokémon ex, this attack does 40 more damage.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=20,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
