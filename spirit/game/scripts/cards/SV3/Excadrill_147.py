from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='db8c02a8-6cb1-5498-952f-3397bff01e47',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Excadrill.Name',
    display_name='Excadrill',
    searchable_by=['Excadrill', 'Stage 1', 'Excadrill'],
    subtypes=['Stage 1'],
    collector_number=147,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name',
    family_id=529,
    abilities=[
        Attack(
            title='Pierce',
            cost={PokemonTypes.METAL: 1},
            damage=60,
        ),
    ],
)
