from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7d327954-78ed-52b0-9662-30cd2d3ee494',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    display_name='Nidoran ♂',
    searchable_by=['Nidoran ♂', 'Basic', 'Nidoran'],
    subtypes=['Basic'],
    collector_number=70,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=32,
    abilities=[
        Attack(
            title='Pheromone Poison',
            game_text='If Nidoran ♀ is on your Bench, the Defending Pokémon is now Poisoned.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Horn Attack',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
