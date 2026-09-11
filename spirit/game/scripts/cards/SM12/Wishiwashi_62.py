from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='35a79266-4218-54c1-a99f-a71ec72354db',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wishiwashi.Name',
    display_name='Wishiwashi',
    searchable_by=['Wishiwashi', 'Basic', 'Wishiwashi'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=746,
    abilities=[
        Ability(
            title='Scatter',
            game_text="At the end of your opponent's turn, if this Pokémon has any damage counters on it, flip a coin. If tails, shuffle this Pokémon and all cards attached to it into your deck.",
            passive=standard_passive("At the end of your opponent's turn, if this Pokémon has any damage counters on it, flip a coin. If tails, shuffle this Pokémon and all cards attached to it into your deck."),
        ),
        Attack(
            title='Hydro Splash',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)
