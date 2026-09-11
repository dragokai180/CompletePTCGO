from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6c2dd2bd-d3ff-59cd-861e-7abefba6bb94',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoOhLEGEND.Name',
    display_name='Ho-Oh LEGEND',
    searchable_by=['Ho-Oh LEGEND', 'LEGEND', 'HoOhLEGEND'],
    subtypes=['LEGEND'],
    collector_number=111,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Legendary,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.LEGEND,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=250,
    abilities=[
        Ability(
            title='Sacred Rainbow',
            game_text='All Energy attached to Ho-Oh LEGEND are Fire Energy instead of their usual type.',
            ability_type=AbilityTypes.POKE_BODY,
            passive=standard_passive('All Energy attached to Ho-Oh LEGEND are Fire Energy instead of their usual type.'),
        ),
        Attack(
            title='Bright Wing',
            game_text='Discard an Energy attached to Ho-Oh LEGEND.',
            cost={PokemonTypes.FIRE: 4},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
