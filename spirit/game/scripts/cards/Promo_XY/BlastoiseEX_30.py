from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='730c1c62-b926-54bc-aca7-c3d542a18bff',
    key='Promo_XY',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name',
    display_name='Blastoise-EX',
    searchable_by=['Blastoise-EX', 'Basic', 'EX', 'BlastoiseEX'],
    subtypes=['Basic', 'EX'],
    collector_number=30,
    set_code='Promo_XY',
    regulation_mark=None,
    rarity=Rarities.RarePromo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=9,
    abilities=[
        Attack(
            title='Rapid Spin',
            game_text='Switch this Pokémon with 1 of your Benched Pokémon. Then, your opponent switches his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Splash Bomb',
            game_text='Flip a coin. If tails, this Pokémon does 30 damage to itself.',
            cost={PokemonTypes.WATER: 3},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
