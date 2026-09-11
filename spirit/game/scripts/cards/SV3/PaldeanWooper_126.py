from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='588f207c-9724-58da-bd9d-fb8dae5fcf75',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name',
    display_name='Paldean Wooper',
    searchable_by=['Paldean Wooper', 'Basic', 'PaldeanWooper'],
    subtypes=['Basic'],
    collector_number=126,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=194,
    abilities=[
        Attack(
            title='Spit Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1},
            effect=standard_attack,
        ),
    ],
)
