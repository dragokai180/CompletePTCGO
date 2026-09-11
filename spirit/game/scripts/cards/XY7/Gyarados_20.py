from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b1f941c1-c5ed-56d6-99b0-767ebda70f96',
    key='XY7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gyarados.Name',
    display_name='Gyarados',
    searchable_by=['Gyarados', 'Stage 1', 'Gyarados'],
    subtypes=['Stage 1'],
    collector_number=20,
    set_code='XY7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name',
    family_id=129,
    abilities=[
        Attack(
            title='Berserker Splash',
            game_text="This attack does 10 damage to each Benched Pokémon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Tail',
            game_text='Flip a coin for each Water Energy attached to this Pokémon. This attack does 30 more damage for each heads.',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 3},
            damage=90,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
