from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6a38bcdd-f128-597f-99f4-676e69bbc319',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cubchoo.Name',
    display_name='Cubchoo',
    searchable_by=['Cubchoo', 'Basic', 'Cubchoo'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=613,
    abilities=[
        Attack(
            title='Smash Kick',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Trip Over',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
