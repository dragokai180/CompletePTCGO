from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='60fad549-a61d-53e6-9d2e-4a7baa3f196f',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name',
    display_name='Grovyle',
    searchable_by=['Grovyle', 'Stage 1', 'Grovyle'],
    subtypes=['Stage 1'],
    collector_number=7,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name',
    family_id=252,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.GRASS: 1},
            damage=20,
        ),
        Attack(
            title='Agility',
            game_text="Flip a coin. If heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
