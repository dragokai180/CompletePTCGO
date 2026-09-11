from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='237e9d02-3d28-5037-b2d1-b51e9c7d25f8',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    display_name='Bellsprout',
    searchable_by=['Bellsprout', 'Basic', 'Bellsprout'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=69,
    abilities=[
        Attack(
            title='Inviting Scent',
            game_text="Switch the Defending Pokémon with 1 of your opponent's Benched Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Careless Tackle',
            game_text='Bellsprout does 10 damage to itself.',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
