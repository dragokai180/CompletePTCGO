from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a120da5-b852-5cae-a42b-321b8789025d',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name',
    display_name='Aipom',
    searchable_by=['Aipom', 'Basic', 'Aipom'],
    subtypes=['Basic'],
    collector_number=90,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=190,
    abilities=[
        Attack(
            title='Fiddle Around',
            game_text="Look at the top 3 cards of your opponent's deck and put them back in any order.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tail Jab',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
