from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a2df052-5c14-56b0-ad61-b16a06fef834',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name',
    display_name='Golett',
    searchable_by=['Golett', 'Basic', 'Golett'],
    subtypes=['Basic'],
    collector_number=34,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=622,
    abilities=[
        Attack(
            title='Smash Punch',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
