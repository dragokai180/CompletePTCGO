from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f2e52d9c-1611-5b62-9eba-d22c0498db9a',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name',
    display_name='Butterfree',
    searchable_by=['Butterfree', 'Stage 2', 'Butterfree'],
    subtypes=['Stage 2'],
    collector_number=16,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name',
    family_id=10,
    abilities=[
        Attack(
            title='Cure Powder',
            game_text='Remove 3 damage counters from each of your Pokémon.',
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Whirlwind',
            game_text='Your opponent switches the Defending Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
