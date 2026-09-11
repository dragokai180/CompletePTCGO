from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fa28f6e4-b3d4-5b24-86ae-f5030b61b976',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Kingler.Name',
    display_name='Kingler',
    searchable_by=['Kingler', 'Stage 1', 'Kingler'],
    subtypes=['Stage 1'],
    collector_number=14,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Krabby.Name',
    family_id=98,
    abilities=[
        Attack(
            title='Guard Claw',
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 20 (after applying Weakness and Resistance).",
            cost={PokemonTypes.WATER: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Crabhammer',
            cost={PokemonTypes.WATER: 4},
            damage=100,
        ),
    ],
)
