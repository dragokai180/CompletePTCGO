from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d57da31-e3ae-508a-9ccb-698173e3b1d9',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Fidough.Name',
    display_name='Fidough',
    searchable_by=['Fidough', 'Basic', 'Fidough'],
    subtypes=['Basic'],
    collector_number=97,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=926,
    abilities=[
        Attack(
            title='Rear Kick',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
