from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5960d499-327f-5316-b013-dd74925fd4f3',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Unfezant.Name',
    display_name='Unfezant',
    searchable_by=['Unfezant', 'Stage 2', 'Unfezant'],
    subtypes=['Stage 2'],
    collector_number=80,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tranquill.Name',
    family_id=519,
    abilities=[
        Attack(
            title='Quick Attack',
            game_text='Flip a coin. If heads, this attack does 30 more damage.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Strong Winds',
            game_text="Shuffle all cards attached to each player's Pokémon into that player's deck.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=standard_attack,
        ),
    ],
)
