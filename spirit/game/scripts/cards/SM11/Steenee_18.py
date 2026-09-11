from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c8c3e694-252c-5083-a0de-9e1851262035',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name',
    display_name='Steenee',
    searchable_by=['Steenee', 'Stage 1', 'Steenee'],
    subtypes=['Stage 1'],
    collector_number=18,
    set_code='SM11',
    regulation_mark=None,
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
            title='Double Slap',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Leaf Step',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
