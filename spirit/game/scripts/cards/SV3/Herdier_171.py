from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6e4b00cb-8f5a-5b0f-a6bd-fad56aea9c07',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name',
    display_name='Herdier',
    searchable_by=['Herdier', 'Stage 1', 'Herdier'],
    subtypes=['Stage 1'],
    collector_number=171,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lillipup.Name',
    family_id=506,
    abilities=[
        Attack(
            title='Rear Kick',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Hammer In',
            cost={PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
