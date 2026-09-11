from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6ec825e5-2024-5e3f-b521-3d6523162877',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Steenee.Name',
    display_name='Steenee',
    searchable_by=['Steenee', 'Stage 1', 'Steenee'],
    subtypes=['Stage 1'],
    collector_number=19,
    set_code='SM1',
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
            title='Sweet Scent',
            game_text='Heal 30 damage from 1 of your Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Stomp',
            game_text='Flip a coin. If heads, this attack does 20 more damage.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
