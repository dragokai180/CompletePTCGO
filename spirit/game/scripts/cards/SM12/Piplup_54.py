from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe4a5a7f-bbfc-5908-942e-ad048720e336',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Piplup.Name',
    display_name='Piplup',
    searchable_by=['Piplup', 'Basic', 'Piplup'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=393,
    abilities=[
        Attack(
            title='Bubble Hold',
            game_text="If the Defending Pokémon is a Basic Pokémon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.WATER: 3},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
