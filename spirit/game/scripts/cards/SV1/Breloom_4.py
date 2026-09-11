from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='15834376-622f-52d5-a861-8c0527e5beae',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Breloom.Name',
    display_name='Breloom',
    searchable_by=['Breloom', 'Stage 1', 'Breloom'],
    subtypes=['Stage 1'],
    collector_number=4,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Shroomish.Name',
    family_id=285,
    abilities=[
        Attack(
            title='Mach Cross',
            cost={PokemonTypes.GRASS: 1},
            damage=60,
        ),
    ],
)
