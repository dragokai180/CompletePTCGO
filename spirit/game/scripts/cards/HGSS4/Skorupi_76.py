from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9d9e0d29-4f21-5125-8b11-e8d3d4e377c7',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skorupi.Name',
    display_name='Skorupi',
    searchable_by=['Skorupi', 'Basic', 'Skorupi'],
    subtypes=['Basic'],
    collector_number=76,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=451,
    abilities=[
        Attack(
            title='Paralyzing Clamp',
            game_text='Flip a coin. If tails, this attack does nothing. If heads, the Defending Pokémon is now Paralyzed.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
