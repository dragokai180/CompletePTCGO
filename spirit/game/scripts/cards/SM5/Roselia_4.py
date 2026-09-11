from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='87334f26-1ea0-5f44-a1ee-8fd46c67092e',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name',
    display_name='Roselia',
    searchable_by=['Roselia', 'Basic', 'Roselia'],
    subtypes=['Basic'],
    collector_number=4,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=315,
    abilities=[
        Attack(
            title='Petal Dance',
            game_text='Flip 3 coins. This attack does 30 damage for each heads. This Pokémon is now Confused.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
