from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec46de5c-7382-5fbd-9542-fd3862178e7a',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name',
    display_name='Popplio',
    searchable_by=['Popplio', 'Basic', 'Popplio'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=728,
    abilities=[
        Attack(
            title='Blot',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
