from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='78cc49d6-a163-59cd-8c82-34a05368e297',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Snorunt.Name',
    display_name='Snorunt',
    searchable_by=['Snorunt', 'Basic', 'Snorunt'],
    subtypes=['Basic'],
    collector_number=37,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=361,
    abilities=[
        Attack(
            title='Icicle',
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)
