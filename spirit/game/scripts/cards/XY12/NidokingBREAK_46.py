from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='712a10ce-132a-5fe9-915c-5d7da6d98786',
    key='XY12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.NidokingBREAK.Name',
    display_name='Nidoking BREAK',
    searchable_by=['Nidoking BREAK', 'BREAK', 'NidokingBREAK'],
    subtypes=['BREAK'],
    collector_number=46,
    set_code='XY12',
    regulation_mark=None,
    rarity=Rarities.BreakRare,
    hp=180,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoking.Name',
    family_id=32,
    abilities=[
        Attack(
            title='Toxic Drill',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 2 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
