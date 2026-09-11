from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='02a7ca5a-1697-58f7-8739-37e099cfa936',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Numel.Name',
    display_name='Numel',
    searchable_by=['Numel', 'Basic', 'Numel'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=322,
    abilities=[
        Attack(
            title='Hot Magma',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
