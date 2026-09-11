from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f9eed24d-ee0f-50fc-a53b-99de3e1925ee',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name',
    display_name='Koffing',
    searchable_by=['Koffing', 'Basic', 'Koffing'],
    subtypes=['Basic'],
    collector_number=73,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=109,
    abilities=[
        Attack(
            title='Foul Odor',
            game_text='Both Active Pokémon are now Confused.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
