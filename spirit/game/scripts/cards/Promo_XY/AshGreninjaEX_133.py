from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8d76a55a-dd34-5d5a-9b85-f6860b1a9bbf',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AshGreninjaEX.Name',
    display_name='Ash-Greninja-EX',
    searchable_by=['Ash-Greninja-EX', 'Basic', 'EX', 'AshGreninjaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=133,
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
            title='Dancing Shuriken',
            game_text="Flip 3 coins. This attack does 20 damage times the number of heads to 1 of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Ninja Blade',
            game_text="This Pokémon can't use Ninja Blade during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
