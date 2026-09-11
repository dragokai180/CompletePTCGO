from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c241e89b-1127-51b5-9cc3-653f6bf7601a',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name',
    display_name='Manectric',
    searchable_by=['Manectric', 'Stage 1', 'Manectric'],
    subtypes=['Stage 1'],
    collector_number=25,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name',
    family_id=309,
    abilities=[
        Attack(
            title='Random Spark',
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Bite',
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
        ),
    ],
)
