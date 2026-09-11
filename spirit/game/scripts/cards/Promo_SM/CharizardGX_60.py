from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3c72fc37-6481-5f47-a3e5-97fa88c7d328',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.CharizardGX.Name',
    display_name='Charizard-GX',
    searchable_by=['Charizard-GX', 'Stage 2', 'GX', 'CharizardGX'],
    subtypes=['Stage 2', 'GX'],
    collector_number=60,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=250,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name',
    family_id=6,
    abilities=[
        Attack(
            title='Wing Attack',
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
        ),
        Attack(
            title='Crimson Storm',
            game_text='Discard 3 Fire Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 3, PokemonTypes.COLORLESS: 2},
            damage=300,
            effect=standard_attack,
        ),
        Attack(
            title='Raging Out-GX',
            game_text="Discard the top 10 cards of your opponent's deck. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
