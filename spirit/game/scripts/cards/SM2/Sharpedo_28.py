from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='31ccccc3-1146-5772-8a71-facfd2788c0e',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sharpedo.Name',
    display_name='Sharpedo',
    searchable_by=['Sharpedo', 'Stage 1', 'Sharpedo'],
    subtypes=['Stage 1'],
    collector_number=28,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name',
    family_id=318,
    abilities=[
        Attack(
            title='Jet Headbutt',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
        ),
    ],
)
