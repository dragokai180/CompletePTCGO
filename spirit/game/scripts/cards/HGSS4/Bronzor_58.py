from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0ccbeeb5-1295-5df4-82fd-bb5435328807',
    key='HGSS4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name',
    display_name='Bronzor',
    searchable_by=['Bronzor', 'Basic', 'Bronzor'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='HGSS4',
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
    family_id=436,
    abilities=[
        Attack(
            title='Iron Defense',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to Bronzor during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
