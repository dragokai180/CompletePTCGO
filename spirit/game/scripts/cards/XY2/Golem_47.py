from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='910d669e-3583-507a-b097-032a70acd00e',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golem.Name',
    display_name='Golem',
    searchable_by=['Golem', 'Stage 2', 'Golem'],
    subtypes=['Stage 2'],
    collector_number=47,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name',
    family_id=74,
    abilities=[
        Attack(
            title='Stone Edge',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Explosion',
            game_text='This Pokémon does 100 damage to itself.',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
