from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5e429ea9-1f56-54a5-b879-2d571ac85f52',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name',
    display_name='Clefairy',
    searchable_by=['Clefairy', 'Basic', 'Clefairy'],
    subtypes=['Basic'],
    collector_number=132,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=35,
    abilities=[
        Attack(
            title='Double Slap',
            game_text='Flip 2 coins. This attack does 10 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
