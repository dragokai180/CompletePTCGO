from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d19ff267-9833-5cca-9e2f-23eb21cb166c',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Azelf.Name',
    display_name='Azelf',
    searchable_by=['Azelf', 'Basic', 'Azelf'],
    subtypes=['Basic'],
    collector_number=142,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=482,
    abilities=[
        Attack(
            title='Shining Eyes',
            game_text="Put 2 damage counters on each of your opponent's Pokémon that has any damage counters on it.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mind Bend',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
