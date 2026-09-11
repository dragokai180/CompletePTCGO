from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3977e539-24e1-58b9-b592-cc64de38d668',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fletchling.Name',
    display_name='Fletchling',
    searchable_by=['Fletchling', 'Basic', 'Fletchling'],
    subtypes=['Basic'],
    collector_number=82,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=661,
    abilities=[
        Attack(
            title='Acrobatics',
            game_text='Flip 2 coins. This attack does 10 more damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
