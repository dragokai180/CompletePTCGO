from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0dec3902-1c35-50a0-ad8a-2d534f08dccb',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name',
    display_name='Misdreavus',
    searchable_by=['Misdreavus', 'Basic', 'Misdreavus'],
    subtypes=['Basic'],
    collector_number=54,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.COLORLESS,
    resistance_amount=20,
    family_id=200,
    abilities=[
        Attack(
            title='Sharpshooting',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 10 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=standard_attack,
        ),
    ],
)
