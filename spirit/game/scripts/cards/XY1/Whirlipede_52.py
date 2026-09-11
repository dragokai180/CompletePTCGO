from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3b73924c-31e3-5d3f-8b75-5fc838e88f7d',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name',
    display_name='Whirlipede',
    searchable_by=['Whirlipede', 'Stage 1', 'Whirlipede'],
    subtypes=['Stage 1'],
    collector_number=52,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Venipede.Name',
    family_id=543,
    abilities=[
        Attack(
            title='Continuous Tumble',
            game_text='Flip a coin until you get tails. This attack does 30 damage times the number of heads.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
