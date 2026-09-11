from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0da30e7c-4af8-5a42-a27f-24d5800f7fa9',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skitty.Name',
    display_name='Skitty',
    searchable_by=['Skitty', 'Basic', 'Skitty'],
    subtypes=['Basic'],
    collector_number=28,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=300,
    abilities=[
        Attack(
            title='Jump On',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
