from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='49e8a607-bf33-5b25-85ad-937b9e7c7ea0',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    display_name='Voltorb',
    searchable_by=['Voltorb', 'Basic', 'Voltorb'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=100,
    abilities=[
        Attack(
            title='Tumbling Attack',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
