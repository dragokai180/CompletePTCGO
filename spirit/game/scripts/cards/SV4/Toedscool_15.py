from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fa9e82cc-0dad-502e-bc3f-a66db74b41ce',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name',
    display_name='Toedscool',
    searchable_by=['Toedscool', 'Basic', 'Toedscool'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=948,
    abilities=[
        Attack(
            title='Clinging Spore',
            game_text='Attach a Basic Grass Energy card from your hand to 1 of your Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Vine Slap',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
