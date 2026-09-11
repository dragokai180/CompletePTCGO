from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a238d9b6-0462-5918-95bc-20c56d5e7c22',
    key='Promo_SM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BuzzwoleGX.Name',
    display_name='Buzzwole-GX',
    searchable_by=['Buzzwole-GX', 'Basic', 'GX', 'Ultra Beast', 'BuzzwoleGX'],
    subtypes=['Basic', 'GX', 'Ultra Beast'],
    collector_number=69,
    set_code='Promo_SM',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=190,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=794,
    abilities=[
        Attack(
            title='Jet Punch',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Knuckle Impact',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=160,
            effect=standard_attack,
        ),
        Attack(
            title='Absorption-GX',
            game_text="This attack does 40 damage for each of your remaining Prize cards. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
            gx=True,
        ),
    ],
)
