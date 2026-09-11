from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8ce40b7e-419f-57a6-8624-87a08c2a3a7a',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grovyle.Name',
    display_name='Grovyle',
    searchable_by=['Grovyle', 'Stage 1', 'Grovyle'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Treecko.Name',
    family_id=252,
    abilities=[
        Ability(
            title='Sunshine Grace',
            game_text='Once during your turn (before your attack), you may search your deck for a Grass Pokémon, reveal it, and put it into your hand. Then, shuffle your deck.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Slicing Blade',
            cost={PokemonTypes.GRASS: 2},
            damage=40,
        ),
    ],
)
