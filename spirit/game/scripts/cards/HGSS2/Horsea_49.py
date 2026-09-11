from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7e2f5917-76f1-56a7-8eb6-bc3acfe7edcd',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    display_name='Horsea',
    searchable_by=['Horsea', 'Basic', 'Horsea'],
    subtypes=['Basic'],
    collector_number=49,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=116,
    abilities=[
        Attack(
            title='Beat',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Fin Smack',
            game_text='Flip 2 coins. This attack does 20 damage times the number of heads.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
