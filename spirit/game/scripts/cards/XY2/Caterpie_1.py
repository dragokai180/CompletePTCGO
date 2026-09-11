from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed979b4d-96e0-5563-9ddf-7511de4b931a',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    display_name='Caterpie',
    searchable_by=['Caterpie', 'Basic', 'Caterpie'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=10,
    abilities=[
        Ability(
            title='Adaptive Evolution',
            game_text='This Pokémon can evolve during your first turn or the turn you play it.',
            passive=standard_passive('This Pokémon can evolve during your first turn or the turn you play it.'),
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
