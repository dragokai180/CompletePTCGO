from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3afe7c7b-0185-516a-8a80-4313c279f2f1',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Inkay.Name',
    display_name='Inkay',
    searchable_by=['Inkay', 'Basic', 'Inkay'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SM10',
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
    family_id=686,
    abilities=[
        Attack(
            title='Perplex',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
)
