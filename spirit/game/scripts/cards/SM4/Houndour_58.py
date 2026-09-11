from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='03cab798-e1f9-5035-b324-d60fbeb1be0e',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name',
    display_name='Houndour',
    searchable_by=['Houndour', 'Basic', 'Houndour'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=228,
    abilities=[
        Attack(
            title='Rear Kick',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
        Attack(
            title='Darkness Fang',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
