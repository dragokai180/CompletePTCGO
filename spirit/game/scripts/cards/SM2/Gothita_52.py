from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e2c8739-adc5-5cc4-a269-40288507eba8',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gothita.Name',
    display_name='Gothita',
    searchable_by=['Gothita', 'Basic', 'Gothita'],
    subtypes=['Basic'],
    collector_number=52,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=574,
    abilities=[
        Attack(
            title='Blown Kiss',
            game_text="Put 1 damage counter on 1 of your opponent's Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
