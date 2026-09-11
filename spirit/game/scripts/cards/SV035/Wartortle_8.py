from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='500d1d87-951c-5584-a3d8-3766ec883d74',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name',
    display_name='Wartortle',
    searchable_by=['Wartortle', 'Stage 1', 'Wartortle'],
    subtypes=['Stage 1'],
    collector_number=8,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name',
    family_id=7,
    abilities=[
        Attack(
            title='Free Diving',
            game_text='Put up to 3 Basic Water Energy cards from your discard pile into your hand.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.WATER: 2},
            damage=50,
        ),
    ],
)
