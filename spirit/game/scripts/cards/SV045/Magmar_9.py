from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cfa37593-e6eb-54ff-96b2-d9084c62acdd',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name',
    display_name='Magmar',
    searchable_by=['Magmar', 'Basic', 'Magmar'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=126,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw a card.',
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Steady Firebreathing',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
