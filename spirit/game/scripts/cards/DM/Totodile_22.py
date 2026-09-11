from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='61941581-ba1f-5382-b3a6-124a130df931',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Totodile.Name',
    display_name='Totodile',
    searchable_by=['Totodile', 'Basic', 'Totodile'],
    subtypes=['Basic'],
    collector_number=22,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=158,
    abilities=[
        Attack(
            title='Leer',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fury Swipes',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.WATER: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
