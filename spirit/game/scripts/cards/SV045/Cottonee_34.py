from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8b21f2e6-4312-5d64-99e0-d28bc54907bd',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name',
    display_name='Cottonee',
    searchable_by=['Cottonee', 'Basic', 'Cottonee'],
    subtypes=['Basic'],
    collector_number=34,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=546,
    abilities=[
        Attack(
            title='Fickle Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
