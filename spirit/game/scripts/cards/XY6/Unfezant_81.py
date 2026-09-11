from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b2653c22-fb05-59ab-8fe8-595c44287507',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name',
    display_name='Unfezant',
    searchable_by=['Unfezant', 'Stage 2', 'Unfezant'],
    subtypes=['Stage 2'],
    collector_number=81,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name',
    family_id=519,
    abilities=[
        Attack(
            title='Feather Dance',
            game_text="During your next turn, each of this Pokémon's attacks does 80 more damage (before applying Weakness and Resistance).",
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Sky Attack',
            game_text='Flip a coin. If tails, this attack does nothing.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('You may play this card from your hand to evolve a Pokémon during your first turn or the turn you play that Pokémon.'),
)
