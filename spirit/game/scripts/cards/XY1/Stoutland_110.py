from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1029a7d6-1112-5e80-9114-ae41298b2876',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Stoutland.Name',
    display_name='Stoutland',
    searchable_by=['Stoutland', 'Stage 2', 'Stoutland'],
    subtypes=['Stage 2'],
    collector_number=110,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Herdier.Name',
    family_id=506,
    abilities=[
        Attack(
            title='Bite Off',
            game_text="If your opponent's Active Pokémon is a Pokémon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Wild Barking',
            game_text="Does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 4},
            damage=80,
            effect=standard_attack,
        ),
    ],
)
