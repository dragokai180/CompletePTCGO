from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c4edc1c4-602e-5131-bacd-77d1202b621d',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Surskit.Name',
    display_name='Surskit',
    searchable_by=['Surskit', 'Basic', 'Surskit'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=283,
    abilities=[
        Attack(
            title='Triple Spin',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
