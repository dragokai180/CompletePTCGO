from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6199f889-ea93-5a60-99e3-7fac205e3a87',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noctowl.Name',
    display_name='Noctowl',
    searchable_by=['Noctowl', 'Stage 1', 'Noctowl'],
    subtypes=['Stage 1'],
    collector_number=107,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Hoothoot.Name',
    family_id=163,
    abilities=[
        Attack(
            title='Hypnoblast',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Night Raid',
            game_text='Your opponent reveals their hand. Discard a Pokémon from it.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
