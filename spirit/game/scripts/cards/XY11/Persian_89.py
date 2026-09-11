from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9f16493-9cfa-5806-a287-275727c28cd1',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name',
    display_name='Persian',
    searchable_by=['Persian', 'Stage 1', 'Persian'],
    subtypes=['Stage 1'],
    collector_number=89,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name',
    family_id=52,
    abilities=[
        Attack(
            title='Raid',
            game_text='If this Pokémon evolved from Meowth during this turn, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
