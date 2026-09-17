from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ed50a51f-d1fb-5b9d-91e7-1030e2b7ba17',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zoroark.Name',
    display_name='Zoroark',
    searchable_by=['Zoroark', 'Stage 1', 'Zoroark'],
    subtypes=['Stage 1'],
    collector_number=96,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zorua.Name',
    family_id=570,
    abilities=[
        Ability(
            title='Nighttime Byway',
            game_text="As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is 2 less.",
            passive=standard_passive("As long as this Pokémon is on your Bench, your Active Pokémon's Retreat Cost is 2 less."),
        ),
        Attack(
            title='Slashing Claw',
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=90,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
