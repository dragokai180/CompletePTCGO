from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3bd65ec4-ebae-54ae-be57-d83d10852b18',
    key='Promo_HGSS',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name',
    display_name='Ho-Oh',
    searchable_by=['Ho-Oh', 'Basic', 'HoOh'],
    subtypes=['Basic'],
    collector_number=1,
    set_code='Promo_HGSS',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'HGSS01'}},
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Attack(
            title='Combustion',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title='Sacred Fire',
            game_text="Flip a coin. If heads, choose 1 of your opponent's Pokémon. This attack does 80 damage to that Pokémon. This attack's damage isn't affected by Weakness or Resistance.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
