from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3d57a4fb-0ea1-548f-8ff9-1dda725536d2',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Skiploom.Name',
    display_name='Skiploom',
    searchable_by=['Skiploom', 'Stage 1', 'Skiploom'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name',
    family_id=187,
    abilities=[
        Attack(
            title='Splash',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
