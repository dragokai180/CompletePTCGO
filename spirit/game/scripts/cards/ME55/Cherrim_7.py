from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed1c3dbc-cbed-5300-9688-fb8fc4d3dd42',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name',
    display_name='Cherrim',
    searchable_by=['Cherrim', 'Stage 1', 'Cherrim'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name',
    family_id=420,
    abilities=[
        Attack(
            title='Energy Gift',
            game_text='Search your deck for up to 2 Basic Energy cards and attach them to your Pokémon in any way you like. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Leafage',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
