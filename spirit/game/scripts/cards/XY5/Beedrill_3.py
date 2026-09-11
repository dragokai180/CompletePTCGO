from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b78e8f3c-6880-5b63-9c91-879ce3e27de8',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name',
    display_name='Beedrill',
    searchable_by=['Beedrill', 'Stage 2', 'Beedrill'],
    subtypes=['Stage 2'],
    collector_number=3,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    family_id=13,
    abilities=[
        Attack(
            title='Allergic Shock',
            game_text='During your next turn, if the Defending Pokémon is damaged by an attack, it is Knocked Out.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Twineedle',
            game_text='Flip 2 coins. This attack does 50 damage times the number of heads.',
            cost={PokemonTypes.GRASS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
