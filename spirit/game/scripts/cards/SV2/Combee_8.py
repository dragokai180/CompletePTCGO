from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='060ca39d-6b57-5b9f-b474-928226929e43',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    display_name='Combee',
    searchable_by=['Combee', 'Basic', 'Combee'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SV2',
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
            title='Double Spin',
            game_text='Flip 2 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
