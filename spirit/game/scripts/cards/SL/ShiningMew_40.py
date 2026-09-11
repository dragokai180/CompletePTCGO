from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='be5b16f5-2943-537f-b351-3546df61a896',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ShiningMew.Name',
    display_name='Shining Mew',
    searchable_by=['Shining Mew', 'Basic', 'ShiningMew'],
    subtypes=['Basic'],
    collector_number=40,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Shining,
    hp=30,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=151,
    abilities=[
        Attack(
            title='Legendary Guidance',
            game_text='Search your deck for up to 2 Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Beam',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
