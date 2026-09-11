from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c52e67e6-21d7-502a-94a0-d0c371c15e2d',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name',
    display_name='Gastly',
    searchable_by=['Gastly', 'Basic', 'Gastly'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=92,
    abilities=[
        Attack(
            title='Allure',
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Will-O-Wisp',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
