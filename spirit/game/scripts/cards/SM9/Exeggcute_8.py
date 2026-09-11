from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7968336c-9a57-5728-9935-6b11cfede431',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name',
    display_name='Exeggcute',
    searchable_by=['Exeggcute', 'Basic', 'Exeggcute'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=102,
    abilities=[
        Attack(
            title='Bullet Seed',
            game_text='Flip 4 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
