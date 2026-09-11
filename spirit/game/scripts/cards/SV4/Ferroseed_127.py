from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4bdea31a-b96e-5947-a302-ca1540c78e52',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ferroseed.Name',
    display_name='Ferroseed',
    searchable_by=['Ferroseed', 'Basic', 'Ferroseed'],
    subtypes=['Basic'],
    collector_number=127,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    family_id=597,
    abilities=[
        Attack(
            title='Spike Sting',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
