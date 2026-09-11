from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3b13d07e-7fb1-59b7-89f2-c2cfc7ec3c02',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name',
    display_name='Cosmog',
    searchable_by=['Cosmog', 'Basic', 'Cosmog'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=789,
    abilities=[
        Attack(
            title='Teleport',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
