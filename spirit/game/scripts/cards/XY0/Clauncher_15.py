from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e635d93-5c16-5145-9730-591a75363030',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Clauncher.Name',
    display_name='Clauncher',
    searchable_by=['Clauncher', 'Basic', 'Clauncher'],
    subtypes=['Basic'],
    collector_number=15,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=692,
    abilities=[
        Attack(
            title='Water Gun',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
