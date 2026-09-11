from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6f2596ac-321d-5607-973d-79f2b2d26765',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scatterbug.Name',
    display_name='Scatterbug',
    searchable_by=['Scatterbug', 'Basic', 'Scatterbug'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=664,
    abilities=[
        Ability(
            title='Adaptive Evolution',
            game_text='This Pokémon can evolve during your first turn or the turn you play it.',
            passive=standard_passive('This Pokémon can evolve during your first turn or the turn you play it.'),
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
