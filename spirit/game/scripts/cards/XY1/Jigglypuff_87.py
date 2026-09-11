from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='001082b4-10d4-5828-a145-064f1ee0e7a4',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jigglypuff.Name',
    display_name='Jigglypuff',
    searchable_by=['Jigglypuff', 'Basic', 'Jigglypuff'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=39,
    abilities=[
        Attack(
            title='Rollout',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Heartfelt Song',
            game_text="Discard a Darkness Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
    ],
)
