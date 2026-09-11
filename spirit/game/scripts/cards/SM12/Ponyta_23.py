from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6afda5f3-13e8-58a7-98d4-a22c4a418d48',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Ponyta.Name',
    display_name='Ponyta',
    searchable_by=['Ponyta', 'Basic', 'Ponyta'],
    subtypes=['Basic'],
    collector_number=23,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    family_id=77,
    abilities=[
        Attack(
            title='Minor Errand-Running',
            game_text='Search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Flare',
            cost={PokemonTypes.FIRE: 1},
            damage=10,
        ),
    ],
)
