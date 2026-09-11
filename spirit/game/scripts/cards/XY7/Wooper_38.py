from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3f0b5cb3-f4dd-5744-890d-c1a29584db28',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name',
    display_name='Wooper',
    searchable_by=['Wooper', 'Basic', 'Wooper'],
    subtypes=['Basic'],
    collector_number=38,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=194,
    abilities=[
        Attack(
            title='Nap',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Wave Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
