from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d52c1e4c-129a-5067-b055-a5d19122f017',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    display_name='Nidoran ♀',
    searchable_by=['Nidoran ♀', 'Basic', 'Nidoran'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=29,
    abilities=[
        Attack(
            title='Growl',
            game_text="During your opponent's next turn, attacks used by the Defending Pokémon do 30 less damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Headbutt',
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
