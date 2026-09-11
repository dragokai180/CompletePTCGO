from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='38f270c3-bb3d-5d7c-b39d-3f8639344335',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Greavard.Name',
    display_name='Greavard',
    searchable_by=['Greavard', 'Basic', 'Greavard'],
    subtypes=['Basic'],
    collector_number=100,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=971,
    abilities=[
        Attack(
            title='Play Rough',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
