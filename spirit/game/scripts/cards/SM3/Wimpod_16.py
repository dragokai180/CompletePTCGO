from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1fbf863b-a548-5f10-8842-9db1e4b33afc',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wimpod.Name',
    display_name='Wimpod',
    searchable_by=['Wimpod', 'Basic', 'Wimpod'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=767,
    abilities=[
        Ability(
            title='Wimp Out',
            game_text='During your first turn, this Pokémon has no Retreat Cost.',
            passive=standard_passive('During your first turn, this Pokémon has no Retreat Cost.'),
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
