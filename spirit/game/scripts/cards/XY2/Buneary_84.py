from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5dc3ea2a-9807-55ae-a4c7-a2e510bd0d6e',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Buneary.Name',
    display_name='Buneary',
    searchable_by=['Buneary', 'Basic', 'Buneary'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=427,
    abilities=[
        Attack(
            title='Bounce',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
