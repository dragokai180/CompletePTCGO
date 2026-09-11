from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fcf07ba2-2279-55cc-9eb1-7621f3edb783',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShiningRayquaza.Name',
    display_name='Shining Rayquaza',
    searchable_by=['Shining Rayquaza', 'Basic', 'ShiningRayquaza'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Shining,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=384,
    abilities=[
        Attack(
            title='Dragon Pulse',
            game_text='Discard the top 2 cards of your deck.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Sky Judgment',
            game_text='Discard 3 Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
