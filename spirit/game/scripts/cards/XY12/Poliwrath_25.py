from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='beaa41bd-f8a1-5325-9618-1d638cdf4d4b',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwrath.Name',
    display_name='Poliwrath',
    searchable_by=['Poliwrath', 'Stage 2', 'Poliwrath'],
    subtypes=['Stage 2'],
    collector_number=25,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Poliwhirl.Name',
    family_id=60,
    abilities=[
        Attack(
            title='Dashing Punch',
            game_text='If this Pokémon was on the Bench and became your Active Pokémon this turn, this attack does 50 more damage.',
            cost={PokemonTypes.WATER: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Whirlpool',
            game_text="Discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.WATER: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
