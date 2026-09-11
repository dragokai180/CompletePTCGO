from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c2737020-8a6e-5c13-8cc2-a3a25e1b91ed',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name',
    display_name='Magnemite',
    searchable_by=['Magnemite', 'Basic', 'Magnemite'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=81,
    abilities=[
        Ability(
            title='Solid Unit',
            game_text="As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's).",
            passive=standard_passive("As long as this Pokémon is on your Bench, prevent all damage done to this Pokémon by attacks (both yours and your opponent's)."),
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
