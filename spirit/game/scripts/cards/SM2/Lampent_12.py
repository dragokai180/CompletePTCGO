from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='95983eae-f260-5dbd-abcb-f3283686dbd9',
    key='SM2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lampent.Name',
    display_name='Lampent',
    searchable_by=['Lampent', 'Stage 1', 'Lampent'],
    subtypes=['Stage 1'],
    collector_number=12,
    set_code='SM2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Litwick.Name',
    family_id=607,
    abilities=[
        Attack(
            title='Will-O-Wisp',
            cost={PokemonTypes.FIRE: 1},
            damage=30,
        ),
    ],
)
