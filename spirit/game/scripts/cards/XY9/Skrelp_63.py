from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5443b24b-27ba-5397-8196-e9e96d19a8dc',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name',
    display_name='Skrelp',
    searchable_by=['Skrelp', 'Basic', 'Skrelp'],
    subtypes=['Basic'],
    collector_number=63,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=690,
    abilities=[
        Attack(
            title='Hide',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
