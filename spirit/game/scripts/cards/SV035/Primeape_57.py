from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f1e38251-166a-5a47-9022-e4a48a5ff6fc',
    key='SV035',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name',
    display_name='Primeape',
    searchable_by=['Primeape', 'Stage 1', 'Primeape'],
    subtypes=['Stage 1'],
    collector_number=57,
    set_code='SV035',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    family_id=56,
    abilities=[
        Attack(
            title='Rant and Rave',
            game_text='This Pokémon is now Confused.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Raging Smash',
            game_text="If this Pokémon isn't Confused, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
