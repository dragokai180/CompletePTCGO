from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='062eb010-9c15-5134-a959-2ddf7b46919a',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Keldeo.Name',
    display_name='Keldeo',
    searchable_by=['Keldeo', 'Basic', 'Keldeo'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=647,
    abilities=[
        Ability(
            title='Justified',
            game_text="This Pokémon's attacks do 50 more damage to your opponent's Darkness Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("This Pokémon's attacks do 50 more damage to your opponent's Darkness Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Sacred Sword',
            game_text="This Pokémon can't use Sacred Sword during your next turn.",
            cost={PokemonTypes.WATER: 3},
            damage=100,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
