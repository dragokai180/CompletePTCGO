from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='541dd69c-6ba5-5c15-8280-e6b04ee7ff2f',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mudbray.Name',
    display_name='Mudbray',
    searchable_by=['Mudbray', 'Basic', 'Mudbray'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=749,
    abilities=[
        Attack(
            title='Double Kick',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
