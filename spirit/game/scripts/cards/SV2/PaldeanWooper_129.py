from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='86c06992-944b-5a13-8335-5231135f1c15',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PaldeanWooper.Name',
    display_name='Paldean Wooper',
    searchable_by=['Paldean Wooper', 'Basic', 'PaldeanWooper'],
    subtypes=['Basic'],
    collector_number=129,
    set_code='SV2',
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
            title='Stampede',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Playful Kick',
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
