from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2efe4472-1082-51fb-b618-ef60a352241b',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Heatran.Name',
    display_name='Heatran',
    searchable_by=['Heatran', 'Basic', 'Heatran'],
    subtypes=['Basic'],
    collector_number=48,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=485,
    abilities=[
        Attack(
            title='Lava Burn',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title='Heat Bazooka',
            game_text='Discard the top 5 cards of your deck.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
