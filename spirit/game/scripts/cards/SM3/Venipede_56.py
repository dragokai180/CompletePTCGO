from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc917d85-89a6-5a4a-b080-669a414a0932',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name',
    display_name='Venipede',
    searchable_by=['Venipede', 'Basic', 'Venipede'],
    subtypes=['Basic'],
    collector_number=56,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=543,
    abilities=[
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
        Attack(
            title='Venoshock',
            game_text="If your opponent's Active Pokémon is Poisoned, this attack does 40 more damage.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
