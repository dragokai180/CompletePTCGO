from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9be10bcf-bc47-5e7e-a195-d2abb5dda420',
    key='Promo_SWSH',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Manaphy.Name',
    display_name='Manaphy',
    searchable_by=['Manaphy', 'Basic', 'Manaphy'],
    subtypes=['Basic'],
    collector_number=275,
    set_code='Promo_SWSH',
    regulation_mark='F',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    attributes={200790: {'type': 'string', 'value': 'SWSH275'}},
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=490,
    abilities=[
        Attack(
            title='Pulling Currents',
            game_text="Your opponent reveals their hand. Put up to 2 Basic Pokémon you find there onto your opponent's Bench.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Bullet',
            game_text="This attack also does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.swsh_promos import configure_promo
configure_promo(card)
