from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='831941b3-97dd-533e-83a7-0a302c2f5b6c',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dhelmise.Name',
    display_name='Dhelmise',
    searchable_by=['Dhelmise', 'Basic', 'Dhelmise'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=781,
    abilities=[
        Attack(
            title='Giga Drain',
            game_text="Heal from this Pokémon the same amount of damage you did to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Powerful Spin',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
