from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='939f85be-294b-591a-b8ac-db9b1e94bf64',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Corsola.Name',
    display_name='Corsola',
    searchable_by=['Corsola', 'Basic', 'Corsola'],
    subtypes=['Basic'],
    collector_number=29,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=222,
    abilities=[
        Attack(
            title='Spike Cannon',
            game_text='Flip 2 coins. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Power Gem',
            cost={PokemonTypes.COLORLESS: 3},
            damage=50,
        ),
    ],
)
