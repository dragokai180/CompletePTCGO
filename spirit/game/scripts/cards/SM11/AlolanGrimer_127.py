from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5521fc30-86ae-53f4-9e7b-7c0467cd2df4',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGrimer.Name',
    display_name='Alolan Grimer',
    searchable_by=['Alolan Grimer', 'Basic', 'AlolanGrimer'],
    subtypes=['Basic'],
    collector_number=127,
    set_code='SM11',
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
            title='Collect',
            game_text='Draw 2 cards.',
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Sludge Bomb',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
    ],
)
