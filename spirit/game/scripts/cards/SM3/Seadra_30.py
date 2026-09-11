from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='fdc29529-c618-5983-a372-85de642d8f89',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Seadra.Name',
    display_name='Seadra',
    searchable_by=['Seadra', 'Stage 1', 'Seadra'],
    subtypes=['Stage 1'],
    collector_number=30,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Horsea.Name',
    family_id=116,
    abilities=[
        Attack(
            title='Water Arrow',
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
    ],
)
