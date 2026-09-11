from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8aaf5b56-d8d6-535a-987f-29e9db869b6d',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TrevenantDusknoirGX.Name',
    display_name='Trevenant & Dusknoir-GX',
    searchable_by=['Trevenant & Dusknoir-GX', 'Basic', 'TAG TEAM', 'GX', 'TrevenantDusknoirGX'],
    subtypes=['Basic', 'TAG TEAM', 'GX'],
    collector_number=217,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=477,
    abilities=[
        Attack(
            title='Night Watch',
            game_text="Choose 2 random cards from your opponent's hand. Your opponent reveals those cards and shuffles them into their deck.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=150,
            effect=standard_attack,
        ),
        Attack(
            title='Pale Moon-GX',
            game_text="At the end of your opponent's next turn, the Defending Pokémon will be Knocked Out. If this Pokémon has at least 1 extra Psychic Energy attached to it (in addition to this attack's cost), discard all Energy from your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            locks_next_turn=True,
            gx=True,
        ),
    ],
)
