from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fc4f70e7-3c5a-5328-8971-2bae7dbd99a2',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Slakoth.Name',
    display_name='Slakoth',
    searchable_by=['Slakoth', 'Basic', 'Slakoth'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=287,
    abilities=[
        Attack(
            title='Big Yawn',
            game_text='Both Active Pokémon are now Asleep.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
