from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='28841631-5970-58e4-a1ac-43d5b91dfe9b',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name',
    display_name='Geodude',
    searchable_by=['Geodude', 'Basic', 'Geodude'],
    subtypes=['Basic'],
    collector_number=87,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=74,
    abilities=[
        Attack(
            title='Defense Curl',
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Rock Throw',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
