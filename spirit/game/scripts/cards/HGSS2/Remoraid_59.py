from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='406798a7-79eb-549b-857a-43eba3b0d551',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Remoraid.Name',
    display_name='Remoraid',
    searchable_by=['Remoraid', 'Basic', 'Remoraid'],
    subtypes=['Basic'],
    collector_number=59,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=223,
    abilities=[
        Attack(
            title='Rain Splash',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
        Attack(
            title='Water Arrow',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
