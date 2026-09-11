from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='47beaee1-765e-5f0f-bc44-8422dc2c5371',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glalie.Name',
    display_name='Glalie',
    searchable_by=['Glalie', 'Stage 1', 'Glalie'],
    subtypes=['Stage 1'],
    collector_number=48,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    family_id=361,
    abilities=[
        Attack(
            title='Ice Fang',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed, and discard an Energy from that Pokémon.",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Frosty Typhoon',
            game_text="This Pokémon can't use Frosty Typhoon during your next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
