from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='56744219-0596-535c-80a2-51fa87d7848c',
    key='XY3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Weepinbell.Name',
    display_name='Weepinbell',
    searchable_by=['Weepinbell', 'Stage 1', 'Weepinbell'],
    subtypes=['Stage 1'],
    collector_number=2,
    set_code='XY3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bellsprout.Name',
    family_id=69,
    abilities=[
        Attack(
            title='Vine Whip',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
        Attack(
            title='Spit Poison',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
