from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1a9a9545-6b40-50d2-b4a2-2e57e8bbd90c',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tsareena.Name',
    display_name='Tsareena',
    searchable_by=['Tsareena', 'Stage 2', 'Tsareena'],
    subtypes=['Stage 2'],
    collector_number=18,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name',
    family_id=761,
    abilities=[
        Attack(
            title='Queenly Heel',
            game_text="During your opponent's next turn, Pokémon can't be played from your opponent's hand to evolve the Defending Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Spinning Kick',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.GRASS: 2},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
