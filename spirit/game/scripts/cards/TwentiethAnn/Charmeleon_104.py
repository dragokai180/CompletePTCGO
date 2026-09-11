from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5aa4c006-3580-5044-b837-21eb2cdfeebb',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    display_name='Charmeleon',
    searchable_by=['Charmeleon', 'Stage 1', 'Charmeleon'],
    subtypes=['Stage 1'],
    collector_number=104,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmander.Name',
    family_id=4,
    abilities=[
        Attack(
            title='Call for Support',
            game_text='Search your deck for a Supporter card, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Slash',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)
