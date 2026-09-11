from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='db78afed-6d11-530e-b144-e5adb6f0e400',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flabb.Name',
    display_name='Flabébé',
    searchable_by=['Flabébé', 'Basic', 'Flabb'],
    subtypes=['Basic'],
    collector_number=101,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=669,
    abilities=[
        Attack(
            title='Wish',
            game_text='Flip a coin. If heads, search your deck for a card and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.FAIRY: 1},
            effect=standard_attack,
        ),
    ],
)
