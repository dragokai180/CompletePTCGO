from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='38c3ba15-9efe-54c8-9c66-b51420ffdecc',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Volbeat.Name',
    display_name='Volbeat',
    searchable_by=['Volbeat', 'Basic', 'Volbeat'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=313,
    abilities=[
        Attack(
            title='Illumisile',
            game_text="If you don't have Illumise in play, this attack does nothing. Choose 1 of your opponent's Benched Pokémon. This attack does 30 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Firefly Light',
            game_text='The Defending Pokémon is now Burned and Confused.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
