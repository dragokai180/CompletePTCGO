from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e2ffbc9f-90ee-5dec-872f-4bf1232484a7',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscruel.Name',
    display_name='Toedscruel',
    searchable_by=['Toedscruel', 'Stage 1', 'Toedscruel'],
    subtypes=['Stage 1'],
    collector_number=26,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Toedscool.Name',
    family_id=948,
    abilities=[
        Attack(
            title='Eerie Tentacles',
            game_text="You may move an Energy from your opponent's Active Pokémon to 1 of their Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Triple Smash',
            game_text='Flip 3 coins. This attack does 80 damage for each heads.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
