from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69b5ce39-396b-5b9a-83a6-1b450560212f',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vaporeon.Name',
    display_name='Vaporeon',
    searchable_by=['Vaporeon', 'Stage 1', 'Vaporeon'],
    subtypes=['Stage 1'],
    collector_number=22,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Ability(
            title='Aqua Effect',
            game_text='Each of your Stage 1 Pokémon in play is now a Water Pokémon in addition to its existing types.',
            passive=standard_passive('Each of your Stage 1 Pokémon in play is now a Water Pokémon in addition to its existing types.'),
        ),
        Attack(
            title='Hydro Splash',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
