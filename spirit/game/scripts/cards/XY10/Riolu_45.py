from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f3778736-093d-5a35-afcc-edc87a80185e',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    display_name='Riolu',
    searchable_by=['Riolu', 'Basic', 'Riolu'],
    subtypes=['Basic'],
    collector_number=45,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=447,
    abilities=[
        Attack(
            title='Double Smash',
            game_text='Flip 2 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
