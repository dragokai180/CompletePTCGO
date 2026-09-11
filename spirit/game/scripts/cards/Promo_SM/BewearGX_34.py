from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cdcefae1-d890-537e-93d1-aa877b231586',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BewearGX.Name',
    display_name='Bewear-GX',
    searchable_by=['Bewear-GX', 'Stage 1', 'GX', 'BewearGX'],
    subtypes=['Stage 1', 'GX'],
    collector_number=34,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Stufful.Name',
    family_id=760,
    abilities=[
        Attack(
            title='Bear Hug',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
            effect=standard_attack,
        ),
        Attack(
            title='Double Impact',
            game_text='Flip 2 coins. This attack does 100 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 4},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Big Throw-GX',
            game_text="Discard your opponent's Active Pokémon and all cards attached to it. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.COLORLESS: 4},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
