from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='022a1258-0d56-5652-ad40-9c2d556425d9',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heatmor.Name',
    display_name='Heatmor',
    searchable_by=['Heatmor', 'Basic', 'Heatmor'],
    subtypes=['Basic'],
    collector_number=24,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=631,
    abilities=[
        Attack(
            title='Odor Sleuth',
            game_text='Flip 2 coins. For each heads, put a card from your discard pile into your hand.',
            cost={PokemonTypes.COLORLESS: 2},
            effect=standard_attack,
        ),
        Attack(
            title='Searing Flame',
            game_text="Your opponent's Active Pokémon is now Burned.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
