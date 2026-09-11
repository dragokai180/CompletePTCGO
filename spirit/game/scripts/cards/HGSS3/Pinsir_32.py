from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='90c73b1a-621d-511c-b72b-df867a27c88d',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pinsir.Name',
    display_name='Pinsir',
    searchable_by=['Pinsir', 'Basic', 'Pinsir'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=127,
    abilities=[
        Attack(
            title='Charging Horn',
            game_text='Flip a coin. If heads, this attack does 10 damage plus 20 more damage.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Guillotine',
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
