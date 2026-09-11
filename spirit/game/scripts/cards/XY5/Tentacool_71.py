from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fbe527c1-2842-58d9-b17c-73cffa55d9c7',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    display_name='Tentacool',
    searchable_by=['Tentacool', 'Basic', 'Tentacool'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=72,
    abilities=[
        Attack(
            title='Psyshot',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
    passive=standard_passive('When this Pokémon is healed, double the amount healed.'),
)
