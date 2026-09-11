from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='79887e0e-2782-5d11-9ca5-093ad292d0f6',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bidoof.Name',
    display_name='Bidoof',
    searchable_by=['Bidoof', 'Basic', 'Bidoof'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=399,
    abilities=[
        Attack(
            title='Hyper Fang',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
