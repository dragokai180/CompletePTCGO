from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="1a778cc0-b28f-53b5-8d9a-496a3c24761a",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Morpekoex.Name",
    display_name="Morpeko ex",
    searchable_by=["Morpeko ex", "Basic", "ex", "Morpekoex"],
    subtypes=["Basic", "ex"],
    collector_number=55,
    set_code="ME5",
    regulation_mark="J",
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=877,
    abilities=[
        Attack(
            title="Wheely Draw",
            game_text="Shuffle your hand into your deck. Then, draw 6 cards.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title="Hangry Blaster",
            game_text="This attack does 40 more damage for each damage counter on this Pokémon.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=40,
            damage_operator="+",
            effect=standard_attack,
        ),
    ],
)
