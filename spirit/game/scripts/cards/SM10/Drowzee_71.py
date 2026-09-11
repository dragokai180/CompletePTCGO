from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4bef3e76-2cdc-569e-a0e9-114cfed7ef66',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name',
    display_name='Drowzee',
    searchable_by=['Drowzee', 'Basic', 'Drowzee'],
    subtypes=['Basic'],
    collector_number=71,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=96,
    abilities=[
        Attack(
            title='Hypnosis',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Psypunch',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
