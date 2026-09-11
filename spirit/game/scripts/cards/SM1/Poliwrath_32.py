from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8bfc9ee7-38c4-526e-bd9f-5b316a5ee085',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name',
    display_name='Poliwrath',
    searchable_by=['Poliwrath', 'Stage 2', 'Poliwrath'],
    subtypes=['Stage 2'],
    collector_number=32,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Split Spiral Punch',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Wake-Up Slap',
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 80 more damage. Then, remove all Special Conditions from that Pokémon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
