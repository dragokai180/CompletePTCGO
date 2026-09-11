from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='395d6a4f-f418-5736-8e30-7e76d431d16e',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name',
    display_name='Mantine',
    searchable_by=['Mantine', 'Basic', 'Mantine'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=226,
    abilities=[
        Attack(
            title='Group Swim',
            game_text='Search your deck for a Water Pokémon, show it to your opponent, and put it into your hand. Shuffle your deck afterward.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Slash',
            game_text="Mantine can't attack during your next turn.",
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
