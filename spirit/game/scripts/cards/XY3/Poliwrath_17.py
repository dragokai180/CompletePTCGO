from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='22f0b2c2-bd7c-562b-a83f-141bdca106e6',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name',
    display_name='Poliwrath',
    searchable_by=['Poliwrath', 'Stage 2', 'Poliwrath'],
    subtypes=['Stage 2'],
    collector_number=17,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Steamroll',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Submission',
            game_text='This Pokémon does 30 damage to itself.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
