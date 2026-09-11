from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='284d61e6-ca11-53dc-8d9d-c8f5c0934f42',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Joltik.Name',
    display_name='Joltik',
    searchable_by=['Joltik', 'Basic', 'Joltik'],
    subtypes=['Basic'],
    collector_number=61,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=595,
    abilities=[
        Attack(
            title='Jolt',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
