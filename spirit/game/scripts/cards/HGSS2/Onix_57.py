from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='36b96225-171b-5881-bd1d-bb54bcea55b9',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name',
    display_name='Onix',
    searchable_by=['Onix', 'Basic', 'Onix'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=95,
    abilities=[
        Attack(
            title='Swing Around',
            game_text='Flip 2 coins. This attack does 20 damage plus 20 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
