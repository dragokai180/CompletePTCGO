from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec6f090f-7b81-50f6-980e-3b97b4082eef',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachu.Name',
    display_name='Pikachu',
    searchable_by=['Pikachu', 'Basic', 'Pikachu'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Volt Tackle',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
