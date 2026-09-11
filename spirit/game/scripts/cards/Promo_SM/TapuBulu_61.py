from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d1f8a989-602f-5c34-88dc-85e464acecf3',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TapuBulu.Name',
    display_name='Tapu Bulu',
    searchable_by=['Tapu Bulu', 'Basic', 'TapuBulu'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=787,
    abilities=[
        Attack(
            title='Horn Leech',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Calm Strike',
            game_text='If you have used your GX attack, this attack does 60 more damage.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
