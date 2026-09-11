from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9bd7471b-c1b8-5d5a-83a3-8efe6e2e7312',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name',
    display_name='Nymble',
    searchable_by=['Nymble', 'Basic', 'Nymble'],
    subtypes=['Basic'],
    collector_number=20,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=919,
    abilities=[
        Attack(
            title='Wild Kick',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
