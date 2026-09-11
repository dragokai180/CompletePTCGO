from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9e9a0d3a-69a9-5740-9bc4-092a722a693e',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name',
    display_name='Pancham',
    searchable_by=['Pancham', 'Basic', 'Pancham'],
    subtypes=['Basic'],
    collector_number=72,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=674,
    abilities=[
        Attack(
            title='Karate Chop',
            game_text='This attack does 10 less damage for each damage counter on this Pokémon.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            damage_operator='-',
            effect=standard_attack,
        ),
    ],
)
