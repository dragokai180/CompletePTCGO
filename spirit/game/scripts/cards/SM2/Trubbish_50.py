from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='42194988-6e61-5ca3-b44a-3c2d9847d55d',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Trubbish.Name',
    display_name='Trubbish',
    searchable_by=['Trubbish', 'Basic', 'Trubbish'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=568,
    abilities=[
        Attack(
            title='Stomp Off',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Drool',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
