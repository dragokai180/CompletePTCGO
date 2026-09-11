from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9c2ecd31-4a1c-5997-b14f-a136405c340b',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name',
    display_name='Tauros',
    searchable_by=['Tauros', 'Basic', 'Tauros'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=128,
    abilities=[
        Attack(
            title='Take Down',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Seething Anger',
            game_text='Flip a coin for each damage counter on this Pokémon. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
