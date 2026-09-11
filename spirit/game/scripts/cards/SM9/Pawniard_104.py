from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='39daee60-c77f-5df9-b279-22fca21d41fb',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pawniard.Name',
    display_name='Pawniard',
    searchable_by=['Pawniard', 'Basic', 'Pawniard'],
    subtypes=['Basic'],
    collector_number=104,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Common,
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
            title='Rigidify',
            game_text="During your opponent's next turn, this Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Scratch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
