from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2a5b169b-698a-59bf-bb56-8be62b8203d7',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name',
    display_name='Wimpod',
    searchable_by=['Wimpod', 'Basic', 'Wimpod'],
    subtypes=['Basic'],
    collector_number=50,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=767,
    abilities=[
        Attack(
            title='Sand Attack',
            game_text="If the Defending Pokémon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack doesn't happen.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
