from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='80d71904-c0e2-5742-aa6a-f3ccc9168017',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    display_name='Stufful',
    searchable_by=['Stufful', 'Basic', 'Stufful'],
    subtypes=['Basic'],
    collector_number=181,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=759,
    abilities=[
        Attack(
            title='Continuous Tumble',
            game_text='Flip a coin until you get tails. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
