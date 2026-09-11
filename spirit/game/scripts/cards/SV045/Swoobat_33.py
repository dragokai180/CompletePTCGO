from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4332a6ef-7ad1-5871-a14d-d8f2e45f3a63',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Swoobat.Name',
    display_name='Swoobat',
    searchable_by=['Swoobat', 'Stage 1', 'Swoobat'],
    subtypes=['Stage 1'],
    collector_number=33,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Woobat.Name',
    family_id=527,
    abilities=[
        Attack(
            title='Attraction Wave',
            game_text="Your opponent's Active Pokémon is now Confused. Put 6 damage counters instead of 3 on that Pokémon for this Special Condition.",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
