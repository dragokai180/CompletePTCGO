from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ada6c40b-c93e-50d7-8130-d71e3ae05bfb',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name',
    display_name='Fletchling',
    searchable_by=['Fletchling', 'Basic', 'Fletchling'],
    subtypes=['Basic'],
    collector_number=163,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=661,
    abilities=[
        Attack(
            title='Nosedive',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
