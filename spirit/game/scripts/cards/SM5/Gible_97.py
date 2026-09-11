from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='88988863-e2e8-5588-89a6-39afe03d6f3b',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gible.Name',
    display_name='Gible',
    searchable_by=['Gible', 'Basic', 'Gible'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=443,
    abilities=[
        Ability(
            title='Rock Hiding',
            game_text='If this Pokémon has any Fighting Energy attached to it, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Fighting Energy attached to it, it has no Retreat Cost.'),
        ),
        Attack(
            title='Gnaw',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
