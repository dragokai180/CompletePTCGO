from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='119a5c27-bb44-5462-98c7-f03d620380d8',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shinx.Name',
    display_name='Shinx',
    searchable_by=['Shinx', 'Basic', 'Shinx'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='XY9',
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
    family_id=403,
    abilities=[
        Attack(
            title='Roar',
            game_text='Your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flop',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)
