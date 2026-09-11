from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='250f6b57-c178-51cd-a598-37e7d7dcf442',
    key='XY6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.GalladeEX.Name',
    display_name='Gallade-EX',
    searchable_by=['Gallade-EX', 'Basic', 'EX', 'GalladeEX'],
    subtypes=['Basic', 'EX'],
    collector_number=34,
    set_code='XY6',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=475,
    abilities=[
        Attack(
            title='Swift Lunge',
            game_text='You may have your opponent switch his or her Active Pokémon with 1 of his or her Benched Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Piercing Prizes',
            game_text='This attack does 20 more damage for each of your remaining Prize cards.',
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
