from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f6f82cba-a618-582a-ba35-502ea7a3d6f2',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    display_name='Cubone',
    searchable_by=['Cubone', 'Basic', 'Cubone'],
    subtypes=['Basic'],
    collector_number=77,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=104,
    abilities=[
        Attack(
            title='Whimsy Tackle',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=standard_attack,
        ),
    ],
)
