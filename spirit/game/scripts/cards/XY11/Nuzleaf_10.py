from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4d9b56fd-aa00-5eba-abef-66f75c68913f',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nuzleaf.Name',
    display_name='Nuzleaf',
    searchable_by=['Nuzleaf', 'Stage 1', 'Nuzleaf'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Seedot.Name',
    family_id=273,
    abilities=[
        Attack(
            title='Harden',
            game_text="During your opponent's next turn, if this Pokémon would be damaged by an attack, prevent that attack's damage done to this Pokémon if that damage is 60 or less.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Razor Leaf',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
