from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5b7b8db4-af93-5958-8ed6-a84d54dcefa8',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Teddiursa.Name',
    display_name='Teddiursa',
    searchable_by=['Teddiursa', 'Basic', 'Teddiursa'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=216,
    abilities=[
        Attack(
            title='Take Down',
            game_text='Teddiursa does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
