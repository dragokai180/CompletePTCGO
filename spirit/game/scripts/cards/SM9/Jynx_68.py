from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='744aa9f0-4eb1-5aea-b9d7-41f7abfdfb1b',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jynx.Name',
    display_name='Jynx',
    searchable_by=['Jynx', 'Basic', 'Jynx'],
    subtypes=['Basic'],
    collector_number=68,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=124,
    abilities=[
        Attack(
            title='Dazzle Dance',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mysterious Dance',
            game_text="For each of your opponent's Benched Pokémon, put 1 damage counter on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
