from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='66cb24d3-9a8b-50b7-b704-b16268c4740a',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgeotto.Name',
    display_name='Pidgeotto',
    searchable_by=['Pidgeotto', 'Stage 1', 'Pidgeotto'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pidgey.Name',
    family_id=16,
    abilities=[
        Attack(
            title='Flap',
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
