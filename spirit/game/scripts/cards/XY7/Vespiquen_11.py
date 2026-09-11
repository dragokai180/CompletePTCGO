from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e0839530-a6ea-5cab-bb46-f24b58ee7091',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name',
    display_name='Vespiquen',
    searchable_by=['Vespiquen', 'Stage 1', 'Vespiquen'],
    subtypes=['Stage 1'],
    collector_number=11,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    family_id=415,
    abilities=[
        Attack(
            title='Bee Drain',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
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
    passive=standard_passive('This Pokémon may have up to 2 Pokémon Tool cards attached to it.'),
)
