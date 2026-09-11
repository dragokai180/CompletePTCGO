from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='df53a30a-5528-5986-983f-c6f5d4f08e71',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name',
    display_name='Zeraora',
    searchable_by=['Zeraora', 'Basic', 'Zeraora'],
    subtypes=['Basic'],
    collector_number=60,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=807,
    abilities=[
        Attack(
            title='Crushing Claw',
            game_text="Discard a Special Energy from your opponent's Active Pokémon.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Discharge',
            game_text='Discard all Lightning Energy from this Pokémon. This attack does 50 damage for each card you discarded in this way.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
