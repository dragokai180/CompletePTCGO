from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="a11e3c4b-adc2-5ada-85bb-dfe8cd896eee",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesComfey.Name",
    display_name="Lillie's Comfey",
    searchable_by=["Lillie's Comfey", "Basic", "LilliesComfey"],
    subtypes=["Basic"],
    collector_number=68,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=764,
    abilities=[
        Attack(
            title="Inviting Flowers",
            game_text="You may search your deck for any number of Basic Lillie's Pokémon and put them onto your Bench. Then, shuffle your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Fade Out",
            game_text="Put this Pokémon and all attached cards into your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
