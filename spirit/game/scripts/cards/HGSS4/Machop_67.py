from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d3cdd615-b062-597d-8559-50f7126b6559',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Machop.Name',
    display_name='Machop',
    searchable_by=['Machop', 'Basic', 'Machop'],
    subtypes=['Basic'],
    collector_number=67,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=66,
    abilities=[
        Attack(
            title='Steady Punch',
            game_text='Flip a coin. If heads, this attack does 10 damage plus 10 more damage.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Mach Cross',
            cost={PokemonTypes.FIGHTING: 3},
            damage=50,
        ),
    ],
)
