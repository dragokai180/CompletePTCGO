from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='346b195f-a1bf-5b02-9a82-249eb10c1b19',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoran.Name',
    display_name='Nidoran ♂',
    searchable_by=['Nidoran ♂', 'Basic', 'Nidoran'],
    subtypes=['Basic'],
    collector_number=43,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=32,
    abilities=[
        Attack(
            title='Double Stab',
            game_text='Flip 2 coins. This attack does 10 damage times the number of heads.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
