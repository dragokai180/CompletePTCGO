from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='87b98eb1-2ad5-5518-81c5-7877878a8f70',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    display_name='Gligar',
    searchable_by=['Gligar', 'Basic', 'Gligar'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=207,
    abilities=[
        Attack(
            title='Rock Cannon',
            game_text='Flip a coin until you get tails. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
