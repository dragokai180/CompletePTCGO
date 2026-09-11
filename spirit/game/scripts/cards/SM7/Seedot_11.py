from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c8b9c23f-338c-5ff2-891f-5a3c9bbbf5dc',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name',
    display_name='Seedot',
    searchable_by=['Seedot', 'Basic', 'Seedot'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=273,
    abilities=[
        Attack(
            title='Hang Down',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Harden',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks if that damage is 40 or less.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
    ],
)
