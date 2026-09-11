from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='54b3d5cf-8c64-5528-a14f-b7127ea6fd13',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name',
    display_name='Hoothoot',
    searchable_by=['Hoothoot', 'Basic', 'Hoothoot'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=163,
    abilities=[
        Attack(
            title='See Through',
            game_text='Your opponent reveals their hand.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Peck',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
