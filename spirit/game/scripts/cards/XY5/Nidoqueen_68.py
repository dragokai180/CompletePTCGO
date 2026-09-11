from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='547ddb53-24e3-586d-bcf4-50e9adc511e8',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Nidoqueen.Name',
    display_name='Nidoqueen',
    searchable_by=['Nidoqueen', 'Stage 2', 'Nidoqueen'],
    subtypes=['Stage 2'],
    collector_number=68,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Nidorina.Name',
    family_id=29,
    abilities=[
        Attack(
            title='Double Kick',
            game_text='Flip 2 coins. This attack does 40 damage times the number of heads.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Poison Fang',
            game_text="Your opponent's Active Pokémon is now Poisoned. Put 2 damage counters instead of 1 on that Pokémon between turns.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
