from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='af1761a0-e89d-5213-93be-62aa2541945b',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    display_name='Exeggcute',
    searchable_by=['Exeggcute', 'Basic', 'Exeggcute'],
    subtypes=['Basic'],
    collector_number=102,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=102,
    abilities=[
        Attack(
            title='Ball Roll',
            game_text='Flip a coin until you get tails. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
