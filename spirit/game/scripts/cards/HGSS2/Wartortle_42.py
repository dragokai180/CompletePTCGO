from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7d4924ec-bfec-5652-b2d4-2c875325f889',
    key='HGSS2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name',
    display_name='Wartortle',
    searchable_by=['Wartortle', 'Stage 1', 'Wartortle'],
    subtypes=['Stage 1'],
    collector_number=42,
    set_code='HGSS2',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name',
    family_id=7,
    abilities=[
        Attack(
            title='Water Arrow',
            game_text="Choose 1 of your opponent's Pokémon. This attack does 20 damage to that Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Surf',
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
