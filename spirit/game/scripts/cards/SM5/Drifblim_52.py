from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='374dfbce-7a08-51d1-b288-a7020b16f202',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name',
    display_name='Drifblim',
    searchable_by=['Drifblim', 'Stage 1', 'Drifblim'],
    subtypes=['Stage 1'],
    collector_number=52,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    family_id=425,
    abilities=[
        Attack(
            title='Damage Transport',
            game_text="Move 4 damage counters from each of your Pokémon to your opponent's Active Pokémon.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Wind Wheel',
            game_text='Your opponent switches their Active Pokémon with 1 of their Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
