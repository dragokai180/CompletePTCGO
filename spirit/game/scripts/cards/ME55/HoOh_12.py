from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15494b14-49f0-51f6-addb-6b66ba983900',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoOh.Name',
    display_name='Ho-Oh',
    searchable_by=['Ho-Oh', 'Basic', 'HoOh'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=250,
    abilities=[
        Attack(
            title='Sacred Breath',
            game_text='Discard all Energy from this Pokémon. Heal all damage from 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIRE: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Fire Wing',
            cost={PokemonTypes.FIRE: 3},
            damage=100,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
