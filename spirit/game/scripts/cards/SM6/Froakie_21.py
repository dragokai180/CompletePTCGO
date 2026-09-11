from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae4d62a9-8b6d-5684-91f7-f022190d9a8a',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Froakie.Name',
    display_name='Froakie',
    searchable_by=['Froakie', 'Basic', 'Froakie'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=656,
    abilities=[
        Ability(
            title='Frubbles',
            game_text='If this Pokémon has any Water Energy attached to it, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Water Energy attached to it, it has no Retreat Cost.'),
        ),
        Attack(
            title='Flop',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
