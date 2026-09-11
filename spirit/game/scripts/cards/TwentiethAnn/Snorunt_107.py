from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='68490bec-9b58-5de6-993c-46a11a59b2af',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    display_name='Snorunt',
    searchable_by=['Snorunt', 'Basic', 'Snorunt'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=361,
    abilities=[
        Attack(
            title='Icy Snow',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
