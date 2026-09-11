from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='caf1a7a7-b02e-58a1-b667-90a5a142ca1c',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name',
    display_name='Wimpod',
    searchable_by=['Wimpod', 'Basic', 'Wimpod'],
    subtypes=['Basic'],
    collector_number=8,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=767,
    abilities=[
        Attack(
            title='Scamper Away',
            game_text='Shuffle this Pokémon and all cards attached to it into your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ram',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
