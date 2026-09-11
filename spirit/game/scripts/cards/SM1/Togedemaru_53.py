from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='42ab2d13-bc6a-57fa-94c9-08d48e757761',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Togedemaru.Name',
    display_name='Togedemaru',
    searchable_by=['Togedemaru', 'Basic', 'Togedemaru'],
    subtypes=['Basic'],
    collector_number=53,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=777,
    abilities=[
        Attack(
            title='Defense Curl',
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Discharge',
            game_text='Discard all Lightning Energy from this Pokémon. This attack does 30 damage for each card you discarded in this way.',
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
