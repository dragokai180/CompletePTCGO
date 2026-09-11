from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7ebfe45a-1ab0-5b4a-be0b-a2a0ad45de1b',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mesprit.Name',
    display_name='Mesprit',
    searchable_by=['Mesprit', 'Basic', 'Mesprit'],
    subtypes=['Basic'],
    collector_number=84,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=481,
    abilities=[
        Attack(
            title='First Contact',
            game_text='Search your deck for up to 3 Basic Pokémon and put them onto your Bench. Then, shuffle your deck.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mumble',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=20,
        ),
    ],
)
