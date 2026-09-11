from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1aed4883-5b9d-5891-b80a-c6c609e2a155',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torkoal.Name',
    display_name='Torkoal',
    searchable_by=['Torkoal', 'Basic', 'Torkoal'],
    subtypes=['Basic'],
    collector_number=16,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=324,
    abilities=[
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
        ),
        Attack(
            title='Flamethrower',
            game_text='Flip a coin. If tails, discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
