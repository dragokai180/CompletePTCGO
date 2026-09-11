from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d680c4af-468c-5961-b0f5-dee954c0d92d',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Voltorb.Name',
    display_name='Voltorb',
    searchable_by=['Voltorb', 'Basic', 'Voltorb'],
    subtypes=['Basic'],
    collector_number=83,
    set_code='HGSS4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=100,
    abilities=[
        Attack(
            title='Magnetic Bomb',
            game_text='Flip a coin. If heads, this attack does 20 damage plus 10 more damage. If tails, Voltorb does 10 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
