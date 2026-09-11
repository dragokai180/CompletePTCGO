from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6f80fe6e-99a8-5010-8d40-4df848a9b7c6',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CrobatBREAK.Name',
    display_name='Crobat BREAK',
    searchable_by=['Crobat BREAK', 'BREAK', 'CrobatBREAK'],
    subtypes=['BREAK'],
    collector_number=181,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Crobat.Name',
    family_id=169,
    abilities=[
        Attack(
            title='Silent Bite',
            game_text="You may leave your opponent's Active Pokémon Paralyzed. If you do, shuffle this Pokémon and all cards attached to into your deck.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
