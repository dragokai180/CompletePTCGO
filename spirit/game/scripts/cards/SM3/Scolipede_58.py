from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5df2599b-352d-5a52-b89a-ef531424a26c',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scolipede.Name',
    display_name='Scolipede',
    searchable_by=['Scolipede', 'Stage 2', 'Scolipede'],
    subtypes=['Stage 2'],
    collector_number=58,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Whirlipede.Name',
    family_id=543,
    abilities=[
        Attack(
            title='Poison Horn',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Steamroller',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.PSYCHIC: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=standard_attack,
        ),
    ],
)
