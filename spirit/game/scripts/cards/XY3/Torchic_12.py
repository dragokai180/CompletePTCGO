from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e3c9a9a9-7a6f-5b74-9ace-24f5699d0248',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name',
    display_name='Torchic',
    searchable_by=['Torchic', 'Basic', 'Torchic'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=255,
    abilities=[
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
