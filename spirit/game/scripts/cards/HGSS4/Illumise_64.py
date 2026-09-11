from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1a8d55aa-aca3-518e-8cf7-defeca90c2bd',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Illumise.Name',
    display_name='Illumise',
    searchable_by=['Illumise', 'Basic', 'Illumise'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=314,
    abilities=[
        Attack(
            title='Sweet Scent',
            game_text='Remove 3 damage counters from 1 of your Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Vulcan Beat',
            game_text='Flip a coin for each Volbeat you have in play. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
