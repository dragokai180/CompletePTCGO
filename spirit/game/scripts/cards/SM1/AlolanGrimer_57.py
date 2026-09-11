from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='908befe7-7fad-5731-b3e9-51c10d6517dd',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name',
    display_name='Alolan Grimer',
    searchable_by=['Alolan Grimer', 'Basic', 'AlolanGrimer'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=88,
    abilities=[
        Attack(
            title='Super Poison Breath',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Pound',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
