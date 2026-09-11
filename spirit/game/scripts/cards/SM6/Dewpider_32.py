from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a94baaf7-0251-52bf-9bcb-e978a80d7033',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dewpider.Name',
    display_name='Dewpider',
    searchable_by=['Dewpider', 'Basic', 'Dewpider'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=751,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Spider Web',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
