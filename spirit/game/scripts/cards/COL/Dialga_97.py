from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8f502f8b-536e-5a34-92f7-8b6073428cee',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name',
    display_name='Dialga',
    searchable_by=['Dialga', 'Basic', 'Dialga'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    attributes={200790: {'type': 'string', 'value': 'SL2'}},
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=483,
    abilities=[
        Attack(
            title='Time Rewind',
            game_text='Shuffle your hand into your deck.',
            cost={PokemonTypes.METAL: 4},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
