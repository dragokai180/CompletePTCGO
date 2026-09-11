from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69c53510-c588-5c82-9aad-b7003dd44dce',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Foongus.Name',
    display_name='Foongus',
    searchable_by=['Foongus', 'Basic', 'Foongus'],
    subtypes=['Basic'],
    collector_number=13,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=590,
    abilities=[
        Attack(
            title='Spore',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
