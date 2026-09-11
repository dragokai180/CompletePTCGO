from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9331d7ee-4f8c-539d-9de8-f92b3efd68b2',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Golett.Name',
    display_name='Golett',
    searchable_by=['Golett', 'Basic', 'Golett'],
    subtypes=['Basic'],
    collector_number=89,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=622,
    abilities=[
        Attack(
            title='Return',
            game_text='You may draw cards until you have 5 cards in your hand.',
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
