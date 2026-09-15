from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a58f79c2-8821-5282-aba7-9ccbec570120',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.JolteonGX.Name',
    display_name='Jolteon-GX',
    searchable_by=['Jolteon-GX', 'Stage 1', 'GX', 'JolteonGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=173,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=200,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name',
    family_id=133,
    abilities=[
        Attack(
            title='Electrobullet',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Head Bolt',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
        ),
        Attack(
            title='Swift Run-GX',
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
            locks_next_turn=False,
            gx=True,
        ),
    ],
)
