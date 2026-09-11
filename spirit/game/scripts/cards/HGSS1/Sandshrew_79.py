from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a08cd873-6b61-5edc-9177-10a5ea9e27a1',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Sandshrew.Name',
    display_name='Sandshrew',
    searchable_by=['Sandshrew', 'Basic', 'Sandshrew'],
    subtypes=['Basic'],
    collector_number=79,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    family_id=27,
    abilities=[
        Attack(
            title='Defense Curl',
            game_text="Flip a coin. If heads, prevent all damage done to Sandshrew by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rollout',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
