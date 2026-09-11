from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b8fb602f-b84b-5317-90c8-4010da67b7c3',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name',
    display_name='Sandygast',
    searchable_by=['Sandygast', 'Basic', 'Sandygast'],
    subtypes=['Basic'],
    collector_number=126,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=769,
    abilities=[
        Attack(
            title='Astonish',
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Hook',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
