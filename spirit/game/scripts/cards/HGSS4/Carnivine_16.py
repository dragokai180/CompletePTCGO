from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e7498c30-258a-54cf-912d-50a5211f0911',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carnivine.Name',
    display_name='Carnivine',
    searchable_by=['Carnivine', 'Basic', 'Carnivine'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.WATER,
    resistance_amount=20,
    family_id=455,
    abilities=[
        Attack(
            title='Saliva Lure',
            game_text="Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Stick and Absorb',
            game_text="Remove 3 damage counters from Carnivine. The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
