from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5740c0d7-3fcd-5970-982a-17cd8166fb85',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kangaskhan.Name',
    display_name='Kangaskhan',
    searchable_by=['Kangaskhan', 'Basic', 'Kangaskhan'],
    subtypes=['Basic'],
    collector_number=47,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=115,
    abilities=[
        Attack(
            title='Parental Fury',
            game_text='Flip a coin until you get tails. This attack does 40 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
