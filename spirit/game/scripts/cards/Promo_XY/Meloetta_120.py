from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='333893ae-8224-5e76-a075-7911a92de8fe',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Meloetta.Name',
    display_name='Meloetta',
    searchable_by=['Meloetta', 'Basic', 'Meloetta'],
    subtypes=['Basic'],
    collector_number=120,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=648,
    abilities=[
        Attack(
            title='Soprano Wave',
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Entrancing Melody',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
