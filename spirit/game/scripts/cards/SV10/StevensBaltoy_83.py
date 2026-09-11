from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="60cc3ee3-2751-57b0-889f-da7fd60ebaea",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StevensBaltoy.Name",
    display_name="Steven's Baltoy",
    searchable_by=["Steven's Baltoy", "Basic", "StevensBaltoy"],
    subtypes=["Basic"],
    collector_number=83,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=343,
    abilities=[
        Attack(
            title="Summoning Sign",
            game_text="Search your deck for up to 2 Basic Steven's Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Psychic Sphere",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
