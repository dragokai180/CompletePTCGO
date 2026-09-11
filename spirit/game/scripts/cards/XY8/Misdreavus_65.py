from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d0bb35df-1317-51bb-b6eb-5442a5cd528e',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name',
    display_name='Misdreavus',
    searchable_by=['Misdreavus', 'Basic', 'Misdreavus'],
    subtypes=['Basic'],
    collector_number=65,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=200,
    abilities=[
        Attack(
            title='Haunt',
            game_text="Put 2 damage counters on your opponent's Active Pokémon.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
