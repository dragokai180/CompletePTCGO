from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9a9a7c8f-5dbe-5d17-870a-d67700c8d0ae',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Glimmet.Name',
    display_name='Glimmet',
    searchable_by=['Glimmet', 'Basic', 'Glimmet'],
    subtypes=['Basic'],
    collector_number=121,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=969,
    abilities=[
        Attack(
            title='Iron Defense',
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pokémon by attacks.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Hang Down',
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)
