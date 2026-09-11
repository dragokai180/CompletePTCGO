from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3ff96604-752e-58a2-b3d2-b16bfd788065',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    display_name='Metapod',
    searchable_by=['Metapod', 'Stage 1', 'Metapod'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Caterpie.Name',
    family_id=10,
    abilities=[
        Ability(
            title='Adaptive Evolution',
            game_text='This Pokémon can evolve during your first turn or the turn you play it.',
            passive=standard_passive('This Pokémon can evolve during your first turn or the turn you play it.'),
        ),
        Attack(
            title='Harden',
            game_text="During your opponent's next turn, if this Pokémon would be damaged by an attack, prevent that attack's damage done to this Pokémon if that damage is 60 or less.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
    ],
)
