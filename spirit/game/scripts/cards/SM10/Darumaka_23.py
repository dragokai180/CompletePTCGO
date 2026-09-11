from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7c4f7edf-85ae-55f0-aff1-727541fb247a',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Darumaka.Name',
    display_name='Darumaka',
    searchable_by=['Darumaka', 'Basic', 'Darumaka'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=554,
    abilities=[
        Attack(
            title='Flame Charge',
            game_text='Search your deck for a Fire Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Flop',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
