from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1d36019-b781-520f-befc-082149682948',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name',
    display_name='Joltik',
    searchable_by=['Joltik', 'Basic', 'Joltik'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=595,
    abilities=[
        Attack(
            title='Flail Around',
            game_text='Flip 3 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
