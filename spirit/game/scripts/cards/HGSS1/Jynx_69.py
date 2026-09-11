from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fc108d0b-5a21-55a5-bc45-7f4f9223b0c6',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name',
    display_name='Jynx',
    searchable_by=['Jynx', 'Basic', 'Jynx'],
    subtypes=['Basic'],
    collector_number=69,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=124,
    abilities=[
        Attack(
            title='Mimic',
            game_text="Shuffle your hand into your deck. Then, draw a number of cards equal to the number of cards in your opponent's hand.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Lick',
            game_text='Flip a coin. If heads, the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
