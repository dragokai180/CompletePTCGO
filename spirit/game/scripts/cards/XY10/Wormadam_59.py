from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d538b433-219e-521f-b942-3794e892ff1a',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wormadam.Name',
    display_name='Wormadam',
    searchable_by=['Wormadam', 'Stage 1', 'Wormadam'],
    subtypes=['Stage 1'],
    collector_number=59,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Burmy.Name',
    family_id=412,
    abilities=[
        Attack(
            title='Strike Back',
            game_text='This attack does 20 damage times the number of damage counters on this Pokémon.',
            cost={PokemonTypes.METAL: 1},
            damage=20,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Iron Head',
            game_text='Flip a coin until you get tails. This attack does 20 more damage for each heads.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
