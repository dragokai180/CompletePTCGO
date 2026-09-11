from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bc7db938-da16-53d4-b9c1-0ec2dc065781',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Shuppet.Name',
    display_name='Shuppet',
    searchable_by=['Shuppet', 'Basic', 'Shuppet'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=353,
    abilities=[
        Attack(
            title='Enveloping Shadow',
            game_text="Flip a coin. If heads, during your opponent's next turn, they can't play any Item cards from their hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
