from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3934e187-7b7f-508b-a298-2d5cca6e81ef',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacruel.Name',
    display_name='Tentacruel',
    searchable_by=['Tentacruel', 'Stage 1', 'Tentacruel'],
    subtypes=['Stage 1'],
    collector_number=50,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    family_id=72,
    abilities=[
        Attack(
            title='Tentavolve',
            game_text='If Tentacruel evolved from Tentacool during this turn, the Defending Pokémon is now Paralyzed and Poisoned.',
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Hyper Beam',
            game_text='Flip a coin. If heads, discard an Energy card attached to the Defending Pokémon.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
