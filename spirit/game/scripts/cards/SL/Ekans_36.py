from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c6a36afb-36f0-5c71-a59e-1fd8cd93348f',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ekans.Name',
    display_name='Ekans',
    searchable_by=['Ekans', 'Basic', 'Ekans'],
    subtypes=['Basic'],
    collector_number=36,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=23,
    abilities=[
        Attack(
            title='Poison Sting',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
