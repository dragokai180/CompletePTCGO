from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='76671314-5df3-5cab-a0b7-f3368a06e65f',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mantine.Name',
    display_name='Mantine',
    searchable_by=['Mantine', 'Basic', 'Mantine'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=226,
    abilities=[
        Ability(
            title='Mantine Surf',
            game_text='If this Pokémon has any Energy attached to it, it has no Retreat Cost.',
            passive=standard_passive('If this Pokémon has any Energy attached to it, it has no Retreat Cost.'),
        ),
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
        ),
    ],
)
