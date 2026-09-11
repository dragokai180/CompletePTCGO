from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='204a26bf-b85c-53bd-bd40-3b09302b8737',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Honedge.Name',
    display_name='Honedge',
    searchable_by=['Honedge', 'Basic', 'Honedge'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=679,
    abilities=[
        Attack(
            title='Continuous Slash',
            game_text='Flip a coin until you get tails. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
