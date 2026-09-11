from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='56efb058-82be-5268-88bf-30433b7e42ab',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    display_name='Croagunk',
    searchable_by=['Croagunk', 'Basic', 'Croagunk'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=453,
    abilities=[
        Attack(
            title='Poison Up',
            game_text='If the Defending Pokémon is Poisoned, put 3 more damage counters on that Pokémon between turns. This effect can be applied more than once.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
