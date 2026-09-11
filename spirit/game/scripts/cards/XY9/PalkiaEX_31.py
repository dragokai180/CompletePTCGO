from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d891a91d-0f55-577b-94c7-f3414805cf62',
    key='XY9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.PalkiaEX.Name',
    display_name='Palkia-EX',
    searchable_by=['Palkia-EX', 'Basic', 'EX', 'PalkiaEX'],
    subtypes=['Basic', 'EX'],
    collector_number=31,
    set_code='XY9',
    regulation_mark=None,
    rarity=Rarities.RareHoloEX,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    family_id=484,
    abilities=[
        Attack(
            title='Aqua Turbo',
            game_text='Search your deck for 2 Water Energy cards and attach them to 1 of your Benched Pokémon. Shuffle your deck afterward.',
            cost={PokemonTypes.WATER: 2},
            damage=40,
            effect=standard_attack,
        ),
        Attack(
            title='Pearl Hurricane',
            game_text="This attack does 30 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.WATER: 4},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
