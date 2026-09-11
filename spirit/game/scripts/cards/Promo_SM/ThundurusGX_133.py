from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2c8f9ca4-0c36-5ddb-bfa2-48a06209792c',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ThundurusGX.Name',
    display_name='Thundurus-GX',
    searchable_by=['Thundurus-GX', 'Basic', 'GX', 'ThundurusGX'],
    subtypes=['Basic', 'GX'],
    collector_number=133,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=642,
    abilities=[
        Attack(
            title='Charge',
            game_text='Search your deck for a Lightning Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Electric Ball',
            cost={PokemonTypes.LIGHTNING: 3},
            damage=140,
        ),
        Attack(
            title='Thundering Hurricane-GX',
            game_text="Flip 4 coins. This attack does 100 damage for each heads. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.LIGHTNING: 3},
            damage=100,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
