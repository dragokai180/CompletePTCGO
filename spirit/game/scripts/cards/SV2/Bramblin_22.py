from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e6816e9-7e3f-5291-a66f-870157fe9b5e',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name',
    display_name='Bramblin',
    searchable_by=['Bramblin', 'Basic', 'Bramblin'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=946,
    abilities=[
        Attack(
            title='Ride the Wind',
            game_text='Flip a coin. If heads, switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
