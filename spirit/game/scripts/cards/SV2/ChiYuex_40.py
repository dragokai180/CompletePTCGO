from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2d4ebb16-c454-5d9d-ab8e-257324250c58',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.ChiYuex.Name',
    display_name='Chi-Yu ex',
    searchable_by=['Chi-Yu ex', 'Basic', 'ex', 'ChiYuex'],
    subtypes=['Basic', 'ex'],
    collector_number=40,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=1004,
    abilities=[
        Attack(
            title='Jealously Singe',
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flame Surge',
            game_text='Choose up to 3 of your Benched Pokémon. For each of those Pokémon, search your deck for a Basic Fire Energy card and attach it to that Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
