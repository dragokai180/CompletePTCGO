from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e1bd8e22-a709-5f09-bda4-22b548e7d442',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kecleon.Name',
    display_name='Kecleon',
    searchable_by=['Kecleon', 'Basic', 'Kecleon'],
    subtypes=['Basic'],
    collector_number=162,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=352,
    abilities=[
        Ability(
            title='Unit Color 3',
            game_text='As long as this Pokémon has Unit Energy FightingDarknessFairy attached to it, it is a Fighting, Darkness, and Fairy Pokémon.',
            passive=standard_passive('As long as this Pokémon has Unit Energy FightingDarknessFairy attached to it, it is a Fighting, Darkness, and Fairy Pokémon.'),
        ),
        Attack(
            title='Gentle Slap',
            cost={PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
