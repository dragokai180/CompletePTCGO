from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2bb5dcea-20a8-5bfd-b557-8f981bce0544',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillish.Name',
    display_name='Vanillish',
    searchable_by=['Vanillish', 'Stage 1', 'Vanillish'],
    subtypes=['Stage 1'],
    collector_number=44,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vanillite.Name',
    family_id=582,
    abilities=[
        Attack(
            title='Frost Smash',
            cost={PokemonTypes.WATER: 2},
            damage=60,
        ),
    ],
)
