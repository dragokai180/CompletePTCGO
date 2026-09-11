from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='55814141-8fe9-56f4-8297-2c8dfd0e47f7',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    display_name='Growlithe',
    searchable_by=['Growlithe', 'Basic', 'Growlithe'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='SV1',
    regulation_mark='G',
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
            title='Relentless Flames',
            game_text='Flip a coin until you get tails. This attack does 30 damage for each heads.',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
