from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ebb8aca8-bdbf-52a7-96df-419be16e0c28',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BeedrillEX.Name',
    display_name='Beedrill-EX',
    searchable_by=['Beedrill-EX', 'Basic', 'EX', 'BeedrillEX'],
    subtypes=['Basic', 'EX'],
    collector_number=157,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    family_id=15,
    abilities=[
        Attack(
            title='Double Scrapper',
            game_text="Discard up to 2 Pokémon Tool cards attached to your opponent's Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Pin Missile',
            game_text='Flip 4 coins. This attack does 40 damage times the number of heads.',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
