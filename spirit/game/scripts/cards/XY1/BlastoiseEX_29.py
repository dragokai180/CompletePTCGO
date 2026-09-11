from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='837cb013-ff62-552b-a6f9-908d196d681d',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.BlastoiseEX.Name',
    display_name='Blastoise-EX',
    searchable_by=['Blastoise-EX', 'Basic', 'EX', 'BlastoiseEX'],
    subtypes=['Basic', 'EX'],
    collector_number=29,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
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
            damage=120,
            effect=standard_attack,
        ),
    ],
)
