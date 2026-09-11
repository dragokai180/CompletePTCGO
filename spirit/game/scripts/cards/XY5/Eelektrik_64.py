from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1d32ec0a-cceb-5a28-96b9-bf4f745c491d',
    key='XY5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name',
    display_name='Eelektrik',
    searchable_by=['Eelektrik', 'Stage 1', 'Eelektrik'],
    subtypes=['Stage 1'],
    collector_number=64,
    set_code='XY5',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name',
    family_id=602,
    abilities=[
        Attack(
            title='Thrash',
            game_text='Flip a coin. If heads, this attack does 20 more damage. If tails, this Pokémon does 20 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
    passive=standard_passive('When this Pokémon is healed, double the amount healed.'),
)
