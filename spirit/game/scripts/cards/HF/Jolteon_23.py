from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='63174793-8553-572f-b0be-94379a58f4cd',
    key='HF',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name',
    display_name='Jolteon',
    searchable_by=['Jolteon', 'Stage 1', 'Jolteon'],
    subtypes=['Stage 1'],
    collector_number=23,
    set_code='HF',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Ability(
            title='Electromagnetic Wall',
            game_text='As long as this Pokémon is your Active Pokémon, whenever your opponent attaches an Energy card from their hand to 1 of their Pokémon, put 2 damage counters on that Pokémon.',
            effect=standard_ability,
            trigger=Triggers.ON_ENERGY_ATTACHED,
        ),
        Attack(
            title='Thunderbolt',
            game_text='Discard all Energy from this Pokémon.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=90,
            effect=standard_attack,
        ),
    ],
)
