from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='92d4250b-2609-5623-b949-bd9ff8a4aab1',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name',
    display_name='Lugia',
    searchable_by=['Lugia', 'Basic', 'Lugia'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=249,
    abilities=[
        Attack(
            title='Elemental Blast',
            game_text='Discard a Fire Energy, a Water Energy, and a Lightning Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=250,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
