from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f7da5a3b-f1f6-5f96-bd6b-13767c674d53',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tatsugiri.Name',
    display_name='Tatsugiri',
    searchable_by=['Tatsugiri', 'Basic', 'Tatsugiri'],
    subtypes=['Basic'],
    collector_number=62,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    weakness_amount=2,
    family_id=978,
    abilities=[
        Attack(
            title='Mise en Place',
            game_text='Search your deck for up to 2 Basic Water Energy cards and attach them to 1 of your Basic Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.WATER: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Curl Up',
            game_text='Put this Pokémon and all attached cards into your hand.',
            cost={PokemonTypes.WATER: 1},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
