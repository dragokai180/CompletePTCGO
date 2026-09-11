from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c4942108-3308-5d42-8e93-675e70806a48',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name',
    display_name='Nincada',
    searchable_by=['Nincada', 'Basic', 'Nincada'],
    subtypes=['Basic'],
    collector_number=9,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=290,
    abilities=[
        Attack(
            title='Slight Intrusion',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
