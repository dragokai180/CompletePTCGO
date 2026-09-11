from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3dbff78-7ea7-590e-8ad4-eab112f53136',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.MimeJr.Name',
    display_name='Mime Jr.',
    searchable_by=['Mime Jr.', 'Basic', 'MimeJr'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=439,
    abilities=[
        Attack(
            title='Mimed Games',
            game_text='Your opponent chooses an attack from 1 of their Pokémon in play. Use the chosen attack as this attack.',
            cost={},
            effect=standard_attack,
        ),
    ],
)
