from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ce6d1541-4555-5679-b539-dc08bcd20102',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Doduo.Name',
    display_name='Doduo',
    searchable_by=['Doduo', 'Basic', 'Doduo'],
    subtypes=['Basic'],
    collector_number=98,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=84,
    abilities=[
        Attack(
            title='Double Hit',
            game_text='Flip 2 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
