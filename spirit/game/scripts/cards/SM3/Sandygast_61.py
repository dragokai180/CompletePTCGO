from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='645f1a38-0987-542f-a246-966d5d4c6c72',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandygast.Name',
    display_name='Sandygast',
    searchable_by=['Sandygast', 'Basic', 'Sandygast'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=769,
    abilities=[
        Attack(
            title='Absorb Life',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
