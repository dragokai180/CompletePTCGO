from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ad6f8038-1236-513e-879b-ea7dcd1b7d1c',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name',
    display_name='Mew',
    searchable_by=['Mew', 'Basic', 'Mew'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=151,
    abilities=[
        Ability(
            title='Memories of Dawn',
            game_text='This Pokémon can use the attacks of any of your Basic Pokémon in play. (You still need the necessary Energy to use each attack.)',
            passive=standard_passive('This Pokémon can use the attacks of any of your Basic Pokémon in play. (You still need the necessary Energy to use each attack.)'),
        ),
        Attack(
            title='Encounter',
            game_text='Search your deck for a Pokémon, reveal it, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
