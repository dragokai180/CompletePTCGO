from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e065da10-c386-5d66-9dc1-4a356bc2ed88',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.WhiteKyurem.Name',
    display_name='White Kyurem',
    searchable_by=['White Kyurem', 'Basic', 'WhiteKyurem'],
    subtypes=['Basic'],
    collector_number=81,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    family_id=646,
    abilities=[
        Attack(
            title='Hyper Beam',
            game_text="Flip a coin. If heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Flare Blizzard',
            game_text="This Pokémon can't use Flare Blizzard during your next turn.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
