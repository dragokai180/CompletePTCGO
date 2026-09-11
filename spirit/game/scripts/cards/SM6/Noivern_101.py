from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='af0d3930-371d-5177-8113-f5771faff1e5',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Noivern.Name',
    display_name='Noivern',
    searchable_by=['Noivern', 'Stage 1', 'Noivern'],
    subtypes=['Stage 1'],
    collector_number=101,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Noibat.Name',
    family_id=714,
    abilities=[
        Attack(
            title='Supersonic',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Resonance',
            game_text="If your opponent's Active Pokémon is Confused, this attack does 70 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
