from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a0e57471-7ac2-5c60-96ca-b476abe8bfa7',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mareanie.Name',
    display_name='Mareanie',
    searchable_by=['Mareanie', 'Basic', 'Mareanie'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=747,
    abilities=[
        Attack(
            title='Poison Sting',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
