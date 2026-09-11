from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e8129fb9-a4ef-59ba-a799-312b2f2c6432',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Simipour.Name',
    display_name='Simipour',
    searchable_by=['Simipour', 'Stage 1', 'Simipour'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Panpour.Name',
    family_id=515,
    abilities=[
        Attack(
            title='Green Fling',
            game_text='Put 3 Grass Energy from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hand Fling',
            game_text='This attack does 10 damage times the number of cards in your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
