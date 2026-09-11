from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b092b28c-6460-56c6-ba14-5655fabb36c2',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Finizen.Name',
    display_name='Finizen',
    searchable_by=['Finizen', 'Basic', 'Finizen'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=963,
    abilities=[
        Attack(
            title='Valiant Evolution',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon. If you do, search your deck for a card that evolves from this Pokémon and put it onto this Pokémon to evolve it. Then, shuffle your deck.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Razor Fin',
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)
