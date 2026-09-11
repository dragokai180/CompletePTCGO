from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2d5696df-3f24-5076-aa5e-a6d5f63548b4',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name',
    display_name='Linoone',
    searchable_by=['Linoone', 'Stage 1', 'Linoone'],
    subtypes=['Stage 1'],
    collector_number=112,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name',
    family_id=263,
    abilities=[
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Dash Attack',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
