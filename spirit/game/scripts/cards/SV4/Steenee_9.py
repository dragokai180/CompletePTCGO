from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='32f5f8b5-8b57-5874-99c6-af6d4636e4d3',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name',
    display_name='Steenee',
    searchable_by=['Steenee', 'Stage 1', 'Steenee'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bounsweet.Name',
    family_id=761,
    abilities=[
        Attack(
            title='Spinning Attack',
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
        Attack(
            title='Double Spin',
            game_text='Flip 2 coins. This attack does 40 damage for each heads.',
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
