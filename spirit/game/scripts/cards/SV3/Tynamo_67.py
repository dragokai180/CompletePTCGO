from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e660cc21-0d5c-56d4-b10e-55a3472597c8',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name',
    display_name='Tynamo',
    searchable_by=['Tynamo', 'Basic', 'Tynamo'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=602,
    abilities=[
        Attack(
            title='Static Shock',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
        ),
        Attack(
            title='Tiny Bolt',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
