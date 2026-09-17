from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3446d538-f393-5b06-8b04-7b0d50c35c2d',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name',
    display_name='Mew',
    searchable_by=['Mew', 'Basic', 'Mew'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=151,
    abilities=[
        Attack(
            title='Psychic',
            game_text="This attack does 40 more damage for each Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
