from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9b9479e1-fbe2-5f5c-967b-aef1c09e48e8',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    display_name='Growlithe',
    searchable_by=['Growlithe', 'Basic', 'Growlithe'],
    subtypes=['Basic'],
    collector_number=17,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=58,
    abilities=[
        Attack(
            title='Hind Kick',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
