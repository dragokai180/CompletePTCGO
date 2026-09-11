from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eb025fad-4695-5aba-b247-e5a61a4edc8a',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name',
    display_name='Pumpkaboo',
    searchable_by=['Pumpkaboo', 'Basic', 'Pumpkaboo'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=710,
    abilities=[
        Attack(
            title='Confuse Ray',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
