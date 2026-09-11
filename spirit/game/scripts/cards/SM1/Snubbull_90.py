from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4b31f03c-bab2-5406-a40e-dcb0de090876',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snubbull.Name',
    display_name='Snubbull',
    searchable_by=['Snubbull', 'Basic', 'Snubbull'],
    subtypes=['Basic'],
    collector_number=90,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=209,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='Flip a coin. If tails, this Pokémon does 10 damage to itself.',
            cost={PokemonTypes.FAIRY: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
