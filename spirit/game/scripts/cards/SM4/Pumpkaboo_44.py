from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7082be1f-ce7f-5489-bc0d-29584ba80b9b',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pumpkaboo.Name',
    display_name='Pumpkaboo',
    searchable_by=['Pumpkaboo', 'Basic', 'Pumpkaboo'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='SM4',
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
            title='Astonish',
            game_text="Choose a random card from your opponent's hand. Your opponent reveals that card and shuffles it into their deck.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
