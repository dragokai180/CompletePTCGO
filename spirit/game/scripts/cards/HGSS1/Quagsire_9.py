from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c681dc7-036a-5728-92fe-8e1912fb17b9',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Quagsire.Name',
    display_name='Quagsire',
    searchable_by=['Quagsire', 'Stage 1', 'Quagsire'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    resistance_type=PokemonTypes.LIGHTNING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Wooper.Name',
    family_id=194,
    abilities=[
        Attack(
            title='Muddy Water',
            game_text="Does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Mud Shot',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 3},
            damage=60,
        ),
    ],
)
