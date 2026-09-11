from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e9de5a8f-ce2e-502e-9e27-c05116c02f5a',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name',
    display_name='Alolan Grimer',
    searchable_by=['Alolan Grimer', 'Basic', 'AlolanGrimer'],
    subtypes=['Basic'],
    collector_number=130,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=88,
    abilities=[
        Attack(
            title='Melt',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Nasty Goo',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
