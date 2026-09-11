from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7f84f678-e9b0-5493-929b-ee844c045047',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tandemaus.Name',
    display_name='Tandemaus',
    searchable_by=['Tandemaus', 'Basic', 'Tandemaus'],
    subtypes=['Basic'],
    collector_number=166,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=924,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw 2 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Gentle Slap',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
