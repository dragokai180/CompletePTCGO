from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fd2e6441-8873-58e4-9111-5440466fffd3',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Magmar.Name',
    display_name='Magmar',
    searchable_by=['Magmar', 'Basic', 'Magmar'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=126,
    abilities=[
        Attack(
            title='Fire Punch',
            cost={PokemonTypes.FIRE: 2},
            damage=30,
        ),
        Attack(
            title='Flamethrower',
            game_text='Discard a Fire Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
