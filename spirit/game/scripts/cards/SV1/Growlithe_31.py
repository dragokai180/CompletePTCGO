from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2af422ad-9423-5871-b66f-add53488c62b',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    display_name='Growlithe',
    searchable_by=['Growlithe', 'Basic', 'Growlithe'],
    subtypes=['Basic'],
    collector_number=31,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=58,
    abilities=[
        Attack(
            title='Stoke',
            game_text='Search your deck for up to 2 Basic Fire Energy cards and attach them to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Fire Claws',
            cost={PokemonTypes.FIRE: 3},
            damage=70,
        ),
    ],
)
