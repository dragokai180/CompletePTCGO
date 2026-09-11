from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='71836ad6-95fd-52c6-a222-266ad195d58a',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name',
    display_name='Magnemite',
    searchable_by=['Magnemite', 'Basic', 'Magnemite'],
    subtypes=['Basic'],
    collector_number=52,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=81,
    abilities=[
        Attack(
            title='Shock Generator',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Lightning Ball',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
