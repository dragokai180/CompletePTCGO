from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e855166b-6c01-5bb2-8e32-87e15b0a39a9',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Yveltal.Name',
    display_name='Yveltal',
    searchable_by=['Yveltal', 'Basic', 'Yveltal'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=717,
    abilities=[
        Ability(
            title='Life-Locked',
            game_text="Your opponent's Active Pokémon can't be healed.",
            passive=standard_passive("Your opponent's Active Pokémon can't be healed."),
        ),
        Attack(
            title='Dark Cutter',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
