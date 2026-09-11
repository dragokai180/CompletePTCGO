from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b7764d26-44a0-5c4c-968b-7a7a0b258f39',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mienfoo.Name',
    display_name='Mienfoo',
    searchable_by=['Mienfoo', 'Basic', 'Mienfoo'],
    subtypes=['Basic'],
    collector_number=96,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=619,
    abilities=[
        Attack(
            title='Low Kick',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Beatdown',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
