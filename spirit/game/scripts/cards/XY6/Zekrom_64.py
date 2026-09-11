from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='83a4c6a7-1b19-54e3-b393-8c44a5887f03',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zekrom.Name',
    display_name='Zekrom',
    searchable_by=['Zekrom', 'Basic', 'Zekrom'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=644,
    abilities=[
        Attack(
            title='Energy Stream',
            game_text='Attach a basic Energy card from your discard pile to this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Electric Ball',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
