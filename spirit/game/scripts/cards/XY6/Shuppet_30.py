from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9efdc946-4b2b-5622-abf5-84d83b63b37a',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name',
    display_name='Shuppet',
    searchable_by=['Shuppet', 'Basic', 'Shuppet'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=353,
    abilities=[
        Attack(
            title='Bleh',
            game_text="Discard a Special Energy attached to 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
