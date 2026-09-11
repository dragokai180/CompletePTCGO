from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fe6ff4a0-04cf-5eea-8513-c7d21123626b',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Litten.Name',
    display_name='Litten',
    searchable_by=['Litten', 'Basic', 'Litten'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=725,
    abilities=[
        Attack(
            title='Singe',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
    ],
)
