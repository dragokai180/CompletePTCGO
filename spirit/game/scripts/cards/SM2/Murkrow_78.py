from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2076dbaa-b5ff-5dec-a55c-d16850cc0e39',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name',
    display_name='Murkrow',
    searchable_by=['Murkrow', 'Basic', 'Murkrow'],
    subtypes=['Basic'],
    collector_number=78,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=198,
    abilities=[
        Attack(
            title='Whirlwind',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
