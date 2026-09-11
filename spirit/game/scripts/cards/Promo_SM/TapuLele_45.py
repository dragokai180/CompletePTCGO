from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3de42148-f79a-5275-a898-22de15932a23',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TapuLele.Name',
    display_name='Tapu Lele',
    searchable_by=['Tapu Lele', 'Basic', 'TapuLele'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=786,
    abilities=[
        Attack(
            title='Psywave',
            game_text="This attack does 20 damage times the amount of Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Magical Swap',
            game_text="Move any number of damage counters on your opponent's Pokémon to their other Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
