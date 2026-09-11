from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5703b5e1-33d3-5d49-9352-caf72c3be070',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tentacool.Name',
    display_name='Tentacool',
    searchable_by=['Tentacool', 'Basic', 'Tentacool'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=72,
    abilities=[
        Attack(
            title='Sludge Shock',
            game_text="The Defending Pokémon can't be healed during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
