from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='67359487-8c6d-5dba-be88-0cfc18df500a',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name',
    display_name='Greavard',
    searchable_by=['Greavard', 'Basic', 'Greavard'],
    subtypes=['Basic'],
    collector_number=104,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=971,
    abilities=[
        Attack(
            title='Graveyard Gamboling',
            game_text='This attack does 10 damage for each Psychic Pokémon in your discard pile.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
