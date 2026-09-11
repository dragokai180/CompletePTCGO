from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0fa3a6d6-7a64-593c-84a0-2d5ff5baba9d',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skarmory.Name',
    display_name='Skarmory',
    searchable_by=['Skarmory', 'Basic', 'Skarmory'],
    subtypes=['Basic'],
    collector_number=21,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=227,
    abilities=[
        Attack(
            title='Steel Coat',
            game_text='Search your deck for a Metal Energy card and attach it to 1 of your Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Razor Wing',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
