from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f82965f8-90b6-5940-9671-5a9ccde6a057',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espurr.Name',
    display_name='Espurr',
    searchable_by=['Espurr', 'Basic', 'Espurr'],
    subtypes=['Basic'],
    collector_number=114,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=677,
    abilities=[
        Attack(
            title='Twinkle',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
