from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7c5664d3-0acf-5b33-b70c-3655cd9a37ff',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Minior.Name',
    display_name='Minior',
    searchable_by=['Minior', 'Basic', 'Minior'],
    subtypes=['Basic'],
    collector_number=124,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=774,
    abilities=[
        Attack(
            title='Shoot Meteors',
            game_text="Discard all Energy from this Pokémon, and this attack does 120 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
