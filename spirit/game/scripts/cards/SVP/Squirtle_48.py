from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7a88a841-1fd6-52ec-81e5-4fdc87c1e702',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name',
    display_name='Squirtle',
    searchable_by=['Squirtle', 'Basic', 'Squirtle'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=7,
    abilities=[
        Attack(
            title='Bubble',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.WATER: 2},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
