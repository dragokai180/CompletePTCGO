from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34691010-2c8d-53db-8ec1-6629b56dc795',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Palkia.Name',
    display_name='Palkia',
    searchable_by=['Palkia', 'Basic', 'Palkia'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=484,
    abilities=[
        Attack(
            title='Wormhole',
            game_text="Switch this Pokémon with 1 of your Benched Pokémon. If you do, switch out your opponent's Active Pokémon to the Bench. (Your opponent chooses the new Active Pokémon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
