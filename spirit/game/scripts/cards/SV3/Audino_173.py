from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a8c74b8a-321f-55a8-8d5e-38d4cb94395f',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Audino.Name',
    display_name='Audino',
    searchable_by=['Audino', 'Basic', 'Audino'],
    subtypes=['Basic'],
    collector_number=173,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=531,
    abilities=[
        Attack(
            title='Find a Friend',
            game_text='Search your deck for a Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slap',
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)
