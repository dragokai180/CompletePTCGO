from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f8f6723e-ffc5-5857-9122-e4587a460e38',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Venonat.Name',
    display_name='Venonat',
    searchable_by=['Venonat', 'Basic', 'Venonat'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=48,
    abilities=[
        Attack(
            title='Radar Eyes',
            game_text='Look at the top 7 cards of your deck and put 1 of them into your hand. Shuffle the other cards back into your deck.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flop',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
