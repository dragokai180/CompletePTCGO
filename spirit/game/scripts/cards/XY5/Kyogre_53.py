from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='07b6e982-303d-5351-872b-b285cfd26484',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kyogre.Name',
    display_name='Kyogre',
    searchable_by=['Kyogre', 'Basic', 'Kyogre'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=382,
    abilities=[
        Attack(
            title='Spring Tides',
            game_text='Flip a coin until you get tails. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Ocean Cyclone',
            game_text="This attack does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
