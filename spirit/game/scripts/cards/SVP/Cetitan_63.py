from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ec5c87a8-3a58-53eb-8a0d-cbabb8dc0b24',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cetitan.Name',
    display_name='Cetitan',
    searchable_by=['Cetitan', 'Stage 1', 'Cetitan'],
    subtypes=['Stage 1'],
    collector_number=63,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name',
    family_id=975,
    abilities=[
        Attack(
            title='Avalanche',
            game_text="This attack also does 10 damage to each of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Rolling Slider',
            game_text='Flip 3 coins. This attack does 100 damage for each heads.',
            cost={PokemonTypes.WATER: 3},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
