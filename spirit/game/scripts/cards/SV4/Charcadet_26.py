from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='1148e2d4-e535-5de7-b112-91acab99c8b2',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name',
    display_name='Charcadet',
    searchable_by=['Charcadet', 'Basic', 'Charcadet'],
    subtypes=['Basic'],
    collector_number=26,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=935,
    abilities=[
        Attack(
            title='Fiery Fighting Spirit',
            game_text='Search your deck for a Basic Fire Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Knuckle Punch',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)
