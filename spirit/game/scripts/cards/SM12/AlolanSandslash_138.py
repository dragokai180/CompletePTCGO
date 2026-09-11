from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='13ff706b-481d-5264-a5ad-cd7326003b97',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandslash.Name',
    display_name='Alolan Sandslash',
    searchable_by=['Alolan Sandslash', 'Stage 1', 'AlolanSandslash'],
    subtypes=['Stage 1'],
    collector_number=138,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name',
    family_id=27,
    abilities=[
        Attack(
            title='Curve Strike',
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Reinforced Needle',
            game_text='If this Pokémon has a Pokémon Tool card attached to it, this attack does 60 more damage.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
