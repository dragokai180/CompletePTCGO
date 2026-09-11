from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e73ae66a-7e0d-51d2-9224-bc1bda0a3622',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name',
    display_name='Lillipup',
    searchable_by=['Lillipup', 'Basic', 'Lillipup'],
    subtypes=['Basic'],
    collector_number=103,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=506,
    abilities=[
        Attack(
            title='Work Up',
            game_text="During your next turn, this Pokémon's attacks do 20 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
