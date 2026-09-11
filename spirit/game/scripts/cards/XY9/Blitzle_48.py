from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6c06fa95-7cd2-5b2b-a1bd-9de33db50718',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name',
    display_name='Blitzle',
    searchable_by=['Blitzle', 'Basic', 'Blitzle'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=522,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
