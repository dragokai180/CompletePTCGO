from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='34dce070-f0d6-5aa4-8c9d-8f6fe8daeb3f',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Electivire.Name',
    display_name='Electivire',
    searchable_by=['Electivire', 'Stage 1', 'Electivire'],
    subtypes=['Stage 1'],
    collector_number=43,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Electabuzz.Name',
    family_id=125,
    abilities=[
        Attack(
            title='Thunder Punch',
            game_text='Flip a coin. If heads, this attack does 60 more damage. If tails, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Giga Impact',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=standard_attack,
        ),
    ],
)
