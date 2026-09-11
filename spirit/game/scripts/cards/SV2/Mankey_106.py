from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb799f7a-d0ac-5633-bdc0-82ad8ee9ccde',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    display_name='Mankey',
    searchable_by=['Mankey', 'Basic', 'Mankey'],
    subtypes=['Basic'],
    collector_number=106,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=56,
    abilities=[
        Attack(
            title='Low Kick',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
        Attack(
            title='Hang Down',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
