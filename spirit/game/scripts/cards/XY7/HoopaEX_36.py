from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2106f4c0-6354-5c3a-b801-31d893995379',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.HoopaEX.Name',
    display_name='Hoopa-EX',
    searchable_by=['Hoopa-EX', 'Basic', 'EX', 'HoopaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=36,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=720,
    abilities=[
        Ability(
            title='Scoundrel Ring',
            game_text='When you play this Pokémon from your hand onto your Bench, you may search your deck for up to 3 Pokémon-EX (except for Hoopa-EX), reveal them, and put them into your hand. Shuffle your deck afterward.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Hyperspace Fury',
            game_text="Discard 2 Energy attached to this Pokémon. This attack does 100 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 3},
            effect=standard_attack,
        ),
    ],
)
