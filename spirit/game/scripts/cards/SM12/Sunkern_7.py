from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec97bfd2-0196-5823-b986-7f317bd8fb29',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sunkern.Name',
    display_name='Sunkern',
    searchable_by=['Sunkern', 'Basic', 'Sunkern'],
    subtypes=['Basic'],
    collector_number=7,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=191,
    abilities=[
        Attack(
            title='Leech Seed',
            game_text='Heal 10 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
