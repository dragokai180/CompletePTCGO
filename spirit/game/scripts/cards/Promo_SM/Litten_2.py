from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='087ed49b-8fec-53a8-9e61-bcaf9df687d3',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name',
    display_name='Litten',
    searchable_by=['Litten', 'Basic', 'Litten'],
    subtypes=['Basic'],
    collector_number=2,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=725,
    abilities=[
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
