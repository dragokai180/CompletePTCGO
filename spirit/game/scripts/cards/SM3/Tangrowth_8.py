from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='41718543-1e23-57b9-9757-50188fb7a689',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tangrowth.Name',
    display_name='Tangrowth',
    searchable_by=['Tangrowth', 'Stage 1', 'Tangrowth'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tangela.Name',
    family_id=114,
    abilities=[
        Attack(
            title='Giga Drain',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Crosswise Whip',
            game_text='Flip 4 coins. This attack does 50 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
