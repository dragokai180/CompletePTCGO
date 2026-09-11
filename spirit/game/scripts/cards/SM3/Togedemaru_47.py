from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c2672121-225d-5b88-86af-759b78302729',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name',
    display_name='Togedemaru',
    searchable_by=['Togedemaru', 'Basic', 'Togedemaru'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=777,
    abilities=[
        Attack(
            title='Rollout',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
        ),
        Attack(
            title='Electrosmash',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
