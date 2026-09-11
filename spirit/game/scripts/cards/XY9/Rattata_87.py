from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ef19344f-57d2-5ab7-8b8c-d127f5bb932f',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name',
    display_name='Rattata',
    searchable_by=['Rattata', 'Basic', 'Rattata'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=19,
    abilities=[
        Attack(
            title='Dangerous Suspicion',
            game_text='Draw a card. Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
