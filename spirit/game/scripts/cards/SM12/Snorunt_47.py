from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c422766-4f98-5032-8b7f-ddcccd1221c5',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    display_name='Snorunt',
    searchable_by=['Snorunt', 'Basic', 'Snorunt'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=361,
    abilities=[
        Attack(
            title='Continuous Headbutt',
            game_text='Flip a coin until you get tails. This attack does 20 damage for each heads.',
            cost={PokemonTypes.WATER: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
