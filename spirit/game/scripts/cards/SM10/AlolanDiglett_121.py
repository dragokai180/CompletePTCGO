from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bb821e90-7fb6-51c1-ba6c-ae6ddd621acf',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanDiglett.Name',
    display_name='Alolan Diglett',
    searchable_by=['Alolan Diglett', 'Basic', 'AlolanDiglett'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=50,
    abilities=[
        Attack(
            title='Ram',
            cost={},
            damage=10,
        ),
    ],
)
