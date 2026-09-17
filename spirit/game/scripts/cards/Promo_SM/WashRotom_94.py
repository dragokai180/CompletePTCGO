from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4ae9eab2-8bea-5bde-aa3e-9404c4b00d6b',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WashRotom.Name',
    display_name='Wash Rotom',
    searchable_by=['Wash Rotom', 'Basic', 'WashRotom'],
    subtypes=['Basic'],
    collector_number=94,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=479,
    abilities=[
        Ability(
            title='Roto Motor',
            game_text="If you have 9 or more Pokémon Tool cards in your discard pile, ignore all Energy in the attack cost of each of this Pokémon's attacks.",
            effect=standard_ability,
        ),
        Attack(
            title='Wash Arrow',
            game_text="This attack does 50 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
