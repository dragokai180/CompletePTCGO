from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fd4299fd-fb29-5807-8e73-70d6a7cc2c30',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name',
    display_name='Torchic',
    searchable_by=['Torchic', 'Basic', 'Torchic'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=255,
    abilities=[
        Attack(
            title='Peck',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
        Attack(
            title='Live Coal',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)
