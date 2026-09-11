from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='42edc780-55b6-53e0-a41e-20c42a3f3095',
    key='TwentiethAnn',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gulpin.Name',
    display_name='Gulpin',
    searchable_by=['Gulpin', 'Basic', 'Gulpin'],
    subtypes=['Basic'],
    collector_number=112,
    set_code='TwentiethAnn',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=316,
    abilities=[
        Attack(
            title="Starvin'",
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
