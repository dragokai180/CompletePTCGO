from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d4dbb93d-4951-523b-86a1-6cefbf6dcc41',
    key='SM7',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Exploud.Name',
    display_name='Exploud',
    searchable_by=['Exploud', 'Stage 2', 'Exploud'],
    subtypes=['Stage 2'],
    collector_number=119,
    set_code='SM7',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Loudred.Name',
    family_id=293,
    abilities=[
        Attack(
            title='Dangerous Concert',
            game_text="This attack does 30 damage to each of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Heavy Impact',
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
        ),
    ],
)
