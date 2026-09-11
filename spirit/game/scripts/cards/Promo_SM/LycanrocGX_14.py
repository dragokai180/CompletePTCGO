from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0d61e758-2a44-5767-b3da-ddcc84805658',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.LycanrocGX.Name',
    display_name='Lycanroc-GX',
    searchable_by=['Lycanroc-GX', 'Stage 1', 'GX', 'LycanrocGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=14,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Rockruff.Name',
    family_id=744,
    abilities=[
        Attack(
            title='Crunch',
            game_text="Discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Accelerock',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title='Lycanfang-GX',
            game_text="Discard 2 Energy from this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
            gx=True,
        ),
    ],
)
