from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4a3a3d49-3a2d-584b-818e-d8187f891380',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pupitar.Name',
    display_name='Pupitar',
    searchable_by=['Pupitar', 'Stage 1', 'Pupitar'],
    subtypes=['Stage 1'],
    collector_number=111,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Larvitar.Name',
    family_id=246,
    abilities=[
        Attack(
            title='Headbutt Bounce',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
