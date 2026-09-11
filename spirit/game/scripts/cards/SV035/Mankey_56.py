from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='85fa455b-d058-59dc-aaa5-65586b07de89',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    display_name='Mankey',
    searchable_by=['Mankey', 'Basic', 'Mankey'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=56,
    abilities=[
        Attack(
            title='Thrash',
            game_text='Flip a coin. If tails, this Pokémon also does 20 damage to itself. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
