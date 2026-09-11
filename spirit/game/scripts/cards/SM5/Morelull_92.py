from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='04e1e207-3d71-5c6d-9c28-32c9474e409a',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Morelull.Name',
    display_name='Morelull',
    searchable_by=['Morelull', 'Basic', 'Morelull'],
    subtypes=['Basic'],
    collector_number=92,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=755,
    abilities=[
        Attack(
            title='Flickering Spores',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
        ),
    ],
)
