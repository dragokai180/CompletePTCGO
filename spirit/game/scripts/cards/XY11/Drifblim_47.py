from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='69de54df-c55c-528e-b885-ba6e0f2a6cdf',
    key='XY11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name',
    display_name='Drifblim',
    searchable_by=['Drifblim', 'Stage 1', 'Drifblim'],
    subtypes=['Stage 1'],
    collector_number=47,
    set_code='XY11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name',
    family_id=425,
    abilities=[
        Attack(
            title='Eerie Wave',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Burst Curse',
            game_text="Discard 2 Energy attached to this Pokémon. Put 8 damage counters on your opponent's Pokémon in any way you like.",
            cost={PokemonTypes.PSYCHIC: 2},
            effect=standard_attack,
        ),
    ],
)
