from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2328ab69-4e02-57b9-a9df-e2bb5e9d96bb',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spewpa.Name',
    display_name='Spewpa',
    searchable_by=['Spewpa', 'Stage 1', 'Spewpa'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name',
    family_id=664,
    abilities=[
        Ability(
            title='Adaptive Evolution',
            game_text='This Pokémon can evolve during your first turn or the turn you play it.',
            passive=standard_passive('This Pokémon can evolve during your first turn or the turn you play it.'),
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
