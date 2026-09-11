from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2549b055-83f5-5a20-a3e0-b2aaa77b810c',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zubat.Name',
    display_name='Zubat',
    searchable_by=['Zubat', 'Basic', 'Zubat'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=41,
    abilities=[
        Attack(
            title='Skill Dive',
            game_text="This attack does 10 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
