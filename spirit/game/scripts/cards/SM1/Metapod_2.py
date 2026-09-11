from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='54808374-fbb7-555a-9660-000b16614b6d',
    key='SM1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    display_name='Metapod',
    searchable_by=['Metapod', 'Stage 1', 'Metapod'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='SM1',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    family_id=10,
    abilities=[
        Attack(
            title='Iron Defense',
            game_text="Flip a coin. If heads, prevent all damage done to this Pokémon by attacks during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bug Bite',
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
        ),
    ],
)
