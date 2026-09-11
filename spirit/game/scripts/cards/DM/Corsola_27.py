from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4f607db8-8ba0-54ac-b265-bfa64688debe',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name',
    display_name='Corsola',
    searchable_by=['Corsola', 'Basic', 'Corsola'],
    subtypes=['Basic'],
    collector_number=27,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=222,
    abilities=[
        Attack(
            title='Bubble Shoot',
            game_text="This attack does 20 damage times the amount of Water Energy attached to this Pokémon to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
