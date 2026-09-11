from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5963bb27-70a0-5fc0-91b3-b486f80897e9',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name',
    display_name='Beedrill',
    searchable_by=['Beedrill', 'Stage 2', 'Beedrill'],
    subtypes=['Stage 2'],
    collector_number=5,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name',
    family_id=13,
    abilities=[
        Attack(
            title='Poison Jab',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Flash Needle',
            game_text="Flip 3 coins. This attack does 40 damage times the number of heads. If all of them are heads, prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn.",
            cost={PokemonTypes.GRASS: 2},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
