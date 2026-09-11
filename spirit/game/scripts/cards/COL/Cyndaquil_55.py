from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='49f2b149-a741-50b1-a3fc-69d3f5221a81',
    key='COL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyndaquil.Name',
    display_name='Cyndaquil',
    searchable_by=['Cyndaquil', 'Basic', 'Cyndaquil'],
    subtypes=['Basic'],
    collector_number=55,
    set_code='COL',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=155,
    abilities=[
        Attack(
            title='Fireworks',
            game_text='Flip a coin. If tails, discard a Fire Energy attached to Cyndaquil.',
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            effect=standard_attack,
        ),
    ],
)
