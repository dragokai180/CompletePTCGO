from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ebd0e3f-f164-5d44-885b-ffe0751c8edb',
    key='XY0',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name',
    display_name='Pawniard',
    searchable_by=['Pawniard', 'Basic', 'Pawniard'],
    subtypes=['Basic'],
    collector_number=19,
    set_code='XY0',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=624,
    abilities=[
        Attack(
            title='Pierce',
            cost={PokemonTypes.METAL: 1},
            damage=10,
        ),
        Attack(
            title='Cut',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
