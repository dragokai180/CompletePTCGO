from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e934577a-1b07-583c-bcd5-9744f9790b01',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name',
    display_name='Misdreavus',
    searchable_by=['Misdreavus', 'Basic', 'Misdreavus'],
    subtypes=['Basic'],
    collector_number=57,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=200,
    abilities=[
        Attack(
            title='Mumble',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title='Dual Draw',
            game_text='Each player draws 3 cards.',
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
