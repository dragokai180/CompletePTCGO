from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='33b71889-daad-5bc9-a62e-61975d312fa3',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name',
    display_name='Staryu',
    searchable_by=['Staryu', 'Basic', 'Staryu'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=120,
    abilities=[
        Attack(
            title='Lunge',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
