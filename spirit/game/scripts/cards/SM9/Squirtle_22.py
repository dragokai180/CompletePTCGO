from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='459e0540-fbe5-5e35-a287-95ceb797cca4',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name',
    display_name='Squirtle',
    searchable_by=['Squirtle', 'Basic', 'Squirtle'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=7,
    abilities=[
        Ability(
            title='Floating Shell',
            game_text='If you have a Stadium card in play, this Pokémon has no Retreat Cost.',
            passive=standard_passive('If you have a Stadium card in play, this Pokémon has no Retreat Cost.'),
        ),
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
