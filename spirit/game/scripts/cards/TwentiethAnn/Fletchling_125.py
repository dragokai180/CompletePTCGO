from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c49eb161-61c7-5d7c-85ab-eb6f552cb1b3',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name',
    display_name='Fletchling',
    searchable_by=['Fletchling', 'Basic', 'Fletchling'],
    subtypes=['Basic'],
    collector_number=125,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=661,
    abilities=[
        Attack(
            title='Warble',
            game_text='Search your deck for up to 2 Fletchling, reveal them, and put them into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
