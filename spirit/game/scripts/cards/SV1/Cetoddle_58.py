from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0774c54b-708f-5c44-942b-ab5cd0c93365',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name',
    display_name='Cetoddle',
    searchable_by=['Cetoddle', 'Basic', 'Cetoddle'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=974,
    abilities=[
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
