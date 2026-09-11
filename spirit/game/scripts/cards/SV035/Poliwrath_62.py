from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e5f0b62e-370d-5d39-baa3-58f8efbf9acb',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name',
    display_name='Poliwrath',
    searchable_by=['Poliwrath', 'Stage 2', 'Poliwrath'],
    subtypes=['Stage 2'],
    collector_number=62,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Bubble Beam',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=50,
            effect=standard_attack,
        ),
        Attack(
            title='Heroic Punch',
            game_text='Flip a coin. If heads, this attack does 150 more damage.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
