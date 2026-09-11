from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='90622f82-1fed-5a43-ae06-e7120adbac4a',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name',
    display_name='Hoppip',
    searchable_by=['Hoppip', 'Basic', 'Hoppip'],
    subtypes=['Basic'],
    collector_number=12,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=187,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
    ],
)
