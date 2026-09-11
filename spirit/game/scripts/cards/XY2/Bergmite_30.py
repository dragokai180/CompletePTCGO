from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e7b4c04f-864d-5727-b69a-a443d80661f8',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bergmite.Name',
    display_name='Bergmite',
    searchable_by=['Bergmite', 'Basic', 'Bergmite'],
    subtypes=['Basic'],
    collector_number=30,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    family_id=712,
    abilities=[
        Attack(
            title='Stomp Off',
            game_text="Discard the top card of your opponent's deck.",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
    ],
)
