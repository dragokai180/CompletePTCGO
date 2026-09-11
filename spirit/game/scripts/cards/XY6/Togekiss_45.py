from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a781d24d-5844-5d8e-96f5-60cc48f96e92',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togekiss.Name',
    display_name='Togekiss',
    searchable_by=['Togekiss', 'Stage 2', 'Togekiss'],
    subtypes=['Stage 2'],
    collector_number=45,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Togetic.Name',
    family_id=175,
    abilities=[
        Attack(
            title='Powerful Slap',
            game_text='Flip a coin for each Energy attached to this Pokémon. This attack does 50 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Aura Sphere',
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
