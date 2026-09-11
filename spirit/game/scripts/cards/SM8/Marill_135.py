from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d84d83b4-3c0d-587f-b1e3-39f0a373a7ea',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name',
    display_name='Marill',
    searchable_by=['Marill', 'Basic', 'Marill'],
    subtypes=['Basic'],
    collector_number=135,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=183,
    abilities=[
        Attack(
            title='Magical Shot',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)
