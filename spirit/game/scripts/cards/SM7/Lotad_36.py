from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0e3ef561-c958-5c4c-b759-b5d7ce449b7f',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lotad.Name',
    display_name='Lotad',
    searchable_by=['Lotad', 'Basic', 'Lotad'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=270,
    abilities=[
        Attack(
            title='Surprise',
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
