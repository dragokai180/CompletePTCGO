from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6d3f1269-284e-5f57-b1bc-10f974a55a2b',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Rowlet.Name',
    display_name='Rowlet',
    searchable_by=['Rowlet', 'Basic', 'Rowlet'],
    subtypes=['Basic'],
    collector_number=153,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=722,
    abilities=[
        Attack(
            title='Leaf Blade',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
