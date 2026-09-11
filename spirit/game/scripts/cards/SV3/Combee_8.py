from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='305b909b-4352-5b43-b728-8f4e74034429',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    display_name='Combee',
    searchable_by=['Combee', 'Basic', 'Combee'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=415,
    abilities=[
        Attack(
            title='Share',
            game_text='Heal 20 damage from 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.GRASS: 2},
            damage=20,
        ),
    ],
)
