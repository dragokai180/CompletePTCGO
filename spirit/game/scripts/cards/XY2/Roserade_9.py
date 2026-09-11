from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4348003f-bad0-5d75-ba0e-0c00b844421f',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Roserade.Name',
    display_name='Roserade',
    searchable_by=['Roserade', 'Stage 1', 'Roserade'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Roselia.Name',
    family_id=315,
    abilities=[
        Attack(
            title='Whiplash',
            game_text="Flip a coin until you get tails. For each heads, discard an Energy attached to your opponent's Active Pokémon.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Mega Drain',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
