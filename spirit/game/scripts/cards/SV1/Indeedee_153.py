from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='dcb445cd-1136-5762-b46e-2048e129f0d8',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Indeedee.Name',
    display_name='Indeedee',
    searchable_by=['Indeedee', 'Basic', 'Indeedee'],
    subtypes=['Basic'],
    collector_number=153,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=876,
    abilities=[
        Attack(
            title='Expert Nurturer',
            game_text='Search your deck for a card that evolves from 1 of your Pokémon and put it onto that Pokémon to evolve it. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hypnoblast',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
