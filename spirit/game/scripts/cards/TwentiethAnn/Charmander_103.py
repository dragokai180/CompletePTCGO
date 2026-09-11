from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4bf9341a-4a67-5618-b9a7-0e17b6b9e5d2',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    display_name='Charmander',
    searchable_by=['Charmander', 'Basic', 'Charmander'],
    subtypes=['Basic'],
    collector_number=103,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=4,
    abilities=[
        Attack(
            title='Playful',
            game_text='Flip a coin. If heads, this attack does 20 damage times the number of damage counters on this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
