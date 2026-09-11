from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='adc4c536-d504-5a88-a8c8-b13ac0bb5211',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name',
    display_name='Skitty',
    searchable_by=['Skitty', 'Basic', 'Skitty'],
    subtypes=['Basic'],
    collector_number=120,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=300,
    abilities=[
        Attack(
            title='Fake Out',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
