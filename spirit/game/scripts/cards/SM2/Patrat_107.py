from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a7659c5-0e60-5cfe-ab0a-00833959bba2',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Patrat.Name',
    display_name='Patrat',
    searchable_by=['Patrat', 'Basic', 'Patrat'],
    subtypes=['Basic'],
    collector_number=107,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=504,
    abilities=[
        Attack(
            title='Glance',
            game_text="Look at the top card of your opponent's deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
