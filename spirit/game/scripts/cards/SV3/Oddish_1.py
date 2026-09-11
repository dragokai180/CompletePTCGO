from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f198d56b-12bc-5414-8246-12ffc0b70fcf',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oddish.Name',
    display_name='Oddish',
    searchable_by=['Oddish', 'Basic', 'Oddish'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=43,
    abilities=[
        Attack(
            title="Feelin' Fine",
            game_text='Draw a card.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Stampede',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
