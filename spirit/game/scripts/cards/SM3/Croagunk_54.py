from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0406949e-639b-50cc-be6f-593872e4ac8d',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    display_name='Croagunk',
    searchable_by=['Croagunk', 'Basic', 'Croagunk'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=453,
    abilities=[
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Frog Hop',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
