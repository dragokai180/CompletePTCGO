from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='aa095f96-d55a-51fb-9a66-2e406dbe0dd3',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nymble.Name',
    display_name='Nymble',
    searchable_by=['Nymble', 'Basic', 'Nymble'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=919,
    abilities=[
        Attack(
            title='Slight Splash',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
        ),
    ],
)
