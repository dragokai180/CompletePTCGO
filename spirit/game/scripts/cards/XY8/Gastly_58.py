from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6bb5a2c0-5099-5da5-b593-95011d51bdd4',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gastly.Name',
    display_name='Gastly',
    searchable_by=['Gastly', 'Basic', 'Gastly'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=92,
    abilities=[
        Attack(
            title='Sleep Poison',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Asleep and Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
