from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='9c4ffe62-3823-5057-8ed0-06092d49c86c',
    key='SM6',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.XerneasGX.Name',
    display_name='Xerneas-GX',
    searchable_by=['Xerneas-GX', 'Basic', 'GX', 'XerneasGX'],
    subtypes=['Basic', 'GX'],
    collector_number=90,
    set_code='SM6',
    regulation_mark=None,
    rarity=Rarities.RareHoloGX,
    hp=180,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=716,
    abilities=[
        Attack(
            title='Overrun',
            game_text="This attack does 20 damage to 1 of your opponent's Benched Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Aurora Horns',
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
        Attack(
            title='Sanctuary-GX',
            game_text="Move all damage counters from each of your Pokémon to your opponent's Active Pokémon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FAIRY: 2, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
            gx=True,
        ),
    ],
)
