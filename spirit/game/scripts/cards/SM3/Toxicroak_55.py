from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='bbef14a1-fd41-5bf4-81a4-2cab9a42438c',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name',
    display_name='Toxicroak',
    searchable_by=['Toxicroak', 'Stage 1', 'Toxicroak'],
    subtypes=['Stage 1'],
    collector_number=55,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name',
    family_id=453,
    abilities=[
        Attack(
            title='Poison Jab',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Poison Boost',
            game_text='If this Pokémon is Poisoned, this attack does 80 more damage. Then, remove that Special Condition from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
