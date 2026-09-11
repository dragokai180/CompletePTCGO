from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='70780b83-d4e1-53d2-a589-659092c8e98d',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name',
    display_name='Carvanha',
    searchable_by=['Carvanha', 'Basic', 'Carvanha'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=318,
    abilities=[
        Attack(
            title='Gnaw Through',
            game_text="Discard all Pokémon Tool cards from your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
