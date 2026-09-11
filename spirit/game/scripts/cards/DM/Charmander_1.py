from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f52c41ba-f85f-51ed-9c8d-14a2877950cc',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    display_name='Charmander',
    searchable_by=['Charmander', 'Basic', 'Charmander'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=4,
    abilities=[
        Attack(
            title='Fire Fang',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
