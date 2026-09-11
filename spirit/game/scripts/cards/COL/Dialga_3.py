from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4161d879-2fc1-5ba1-9d45-47749b003aab',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dialga.Name',
    display_name='Dialga',
    searchable_by=['Dialga', 'Basic', 'Dialga'],
    subtypes=['Basic'],
    collector_number=3,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
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
