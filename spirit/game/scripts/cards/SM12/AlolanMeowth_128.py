from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='33c93a36-0016-51b5-ac2b-3f2a5e31588b',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanMeowth.Name',
    display_name='Alolan Meowth',
    searchable_by=['Alolan Meowth', 'Basic', 'AlolanMeowth'],
    subtypes=['Basic'],
    collector_number=128,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=52,
    abilities=[
        Attack(
            title='Swagger',
            game_text="Flip a coin. If heads, discard an Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hook',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
