from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ab525caf-19e5-56d4-9a69-aaa0156e3f40',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name',
    display_name='Alolan Geodude',
    searchable_by=['Alolan Geodude', 'Basic', 'AlolanGeodude'],
    subtypes=['Basic'],
    collector_number=32,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=74,
    abilities=[
        Attack(
            title='Defense Curl',
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={},
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
