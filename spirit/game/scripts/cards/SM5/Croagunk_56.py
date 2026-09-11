from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0c331173-0a0d-53e0-9082-c0aa73d4ec06',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    display_name='Croagunk',
    searchable_by=['Croagunk', 'Basic', 'Croagunk'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='SM5',
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
            title='Swagger',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
