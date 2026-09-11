from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70e102e6-b0b4-50f2-937f-f9cffa75dac7',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name',
    display_name='Carnivine',
    searchable_by=['Carnivine', 'Basic', 'Carnivine'],
    subtypes=['Basic'],
    collector_number=46,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=455,
    abilities=[
        Attack(
            title='Drawup Power',
            game_text='Search your deck for an Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spit Up',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
