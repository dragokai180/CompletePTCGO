from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f64ed985-54ae-59da-a038-6cc93e1c9520',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name',
    display_name='Squirtle',
    searchable_by=['Squirtle', 'Basic', 'Squirtle'],
    subtypes=['Basic'],
    collector_number=33,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=7,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
