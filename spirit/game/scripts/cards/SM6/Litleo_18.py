from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ce905714-fae0-5810-833e-cb75fbd813e0',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litleo.Name',
    display_name='Litleo',
    searchable_by=['Litleo', 'Basic', 'Litleo'],
    subtypes=['Basic'],
    collector_number=18,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=667,
    abilities=[
        Attack(
            title='Headbutt',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
