from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ef43aa7e-d176-50ce-912f-3809e62710fd',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    display_name='Marill',
    searchable_by=['Marill', 'Basic', 'Marill'],
    subtypes=['Basic'],
    collector_number=76,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=183,
    abilities=[
        Attack(
            title='Bubble Drain',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.FAIRY: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
