from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='3efc9b16-f922-5b95-b23c-47759843b5ca',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GreninjaEX.Name',
    display_name='Greninja-EX',
    searchable_by=['Greninja-EX', 'Basic', 'EX', 'GreninjaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=20,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=658,
    abilities=[
        Attack(
            title='Sharpshooting',
            game_text="This attack does 30 damage to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Aqua Blast',
            game_text='Discard 1 Water Energy attached to this Pokémon.',
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
