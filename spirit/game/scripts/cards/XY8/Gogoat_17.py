from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a749e067-1fb7-5433-ac43-0b70242a2093',
    key='XY8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gogoat.Name',
    display_name='Gogoat',
    searchable_by=['Gogoat', 'Stage 1', 'Gogoat'],
    subtypes=['Stage 1'],
    collector_number=17,
    set_code='XY8',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skiddo.Name',
    family_id=672,
    abilities=[
        Attack(
            title='Overrun',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=standard_attack,
        ),
        Attack(
            title='Horn Leech',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.GRASS: 3},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
