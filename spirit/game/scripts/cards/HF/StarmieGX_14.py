from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7d149e4-8444-588c-b9f5-ee82a38fd280',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.StarmieGX.Name',
    display_name='Starmie-GX',
    searchable_by=['Starmie-GX', 'Stage 1', 'GX', 'StarmieGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=14,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=190,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    family_id=120,
    abilities=[
        Attack(
            title='Star Stream',
            game_text='Attach 2 Water Energy cards from your discard pile to 1 of your Pokémon.',
            cost={PokemonTypes.WATER: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.COLORLESS: 3},
            damage=100,
        ),
        Attack(
            title='Hydro Pump-GX',
            game_text="This attack does 40 more damage times the amount of Water Energy attached to this Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='+',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
