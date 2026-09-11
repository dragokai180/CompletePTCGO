from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4d5fa73e-5cee-5deb-ba4c-449db8eabf9a',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    display_name='Skiddo',
    searchable_by=['Skiddo', 'Basic', 'Skiddo'],
    subtypes=['Basic'],
    collector_number=11,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=672,
    abilities=[
        Attack(
            title='Take Down',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.GRASS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
