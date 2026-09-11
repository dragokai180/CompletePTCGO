from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='67f33ecc-e29a-5a0b-8147-5e516ddb5707',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Mareep.Name',
    display_name='Mareep',
    searchable_by=['Mareep', 'Basic', 'Mareep'],
    subtypes=['Basic'],
    collector_number=76,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=179,
    abilities=[
        Attack(
            title='Thunder Shock',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
