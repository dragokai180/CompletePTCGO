from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a5544e39-b8dd-5185-a899-2b3d4ae30510',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pancham.Name',
    display_name='Pancham',
    searchable_by=['Pancham', 'Basic', 'Pancham'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=674,
    abilities=[
        Attack(
            title='Act Tough',
            game_text='If this Pokémon has any Darkness Energy attached to it, this attack does 30 more damage.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
