from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ae8890a1-d3f2-5696-8ede-af04a95cd9a9',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solrock.Name',
    display_name='Solrock',
    searchable_by=['Solrock', 'Basic', 'Solrock'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=338,
    abilities=[
        Ability(
            title='Sunbeam',
            game_text='The maximum HP of each of your Lunatone in play is 130.',
            passive=standard_passive('The maximum HP of each of your Lunatone in play is 130.'),
        ),
        Attack(
            title='Scorching Light',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed. If tails, your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
